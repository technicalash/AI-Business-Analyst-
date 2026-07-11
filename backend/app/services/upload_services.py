from pathlib import Path
import shutil
import uuid
import pandas as pd

from fastapi import UploadFile, HTTPException
from app.services.cleaning_services import clean_dataset
from app.services.analysis_services import analyze_dataset  
from app.services.ai_planner_services import generate_preprocessing_plan  
from app.services.preprocessing_executor import execute_preprocessing_plan  
from app.core.paths import PROCESSED_DIR
from app.services.visualization_planner_services import generate_visualization_plan
from app.services.visualization_executor import execute_visualization_plan
from app.services.session_services import (reset_context, update_context, get_context)
from app.services.statistics_generator import generate_plot_statistics
from app.services.insight_generator import generate_insights


ALLOWED_EXTENSIONS = {".csv"}

# Base directory (backend/)
BASE_DIR = Path(__file__).resolve().parents[2]

# Upload directory
UPLOAD_DIR = BASE_DIR / "storage" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def process_uploaded_file(file : UploadFile):
    
    reset_context()
    _validate_file(file)
    
    file_path, unique_filename = _save_file(file)
    df = _read_csv(file_path)
    df = clean_dataset(df)
    original_metadata  = analyze_dataset(df)
    update_context("original_metadata", original_metadata)
    preprocessing_plan = generate_preprocessing_plan(original_metadata )
    update_context("preprocessing_plan", preprocessing_plan )
    df = execute_preprocessing_plan(df, preprocessing_plan)
    processed_file_path=_save_processed_file(df, unique_filename)
    cleaned_metadata=analyze_dataset(df)
    update_context("cleaned_metadata", cleaned_metadata )
    visualization_plan=generate_visualization_plan(cleaned_metadata)
    update_context("visualization_plan", visualization_plan )
    generated_plots=execute_visualization_plan(df,visualization_plan)
    update_context("generated_plots", generated_plots )
    plot_statistics = generate_plot_statistics(df,visualization_plan)
    update_context("plot_statistics", plot_statistics)
    insights=generate_insights(cleaned_metadata, plot_statistics)
    update_context("insights", insights)
    return {
    "message": "Dataset uploaded and preprocessed successfully.",
    "processed_filename": unique_filename,
    "preprocessing_report": preprocessing_plan,
    "visualization_plan":visualization_plan,
    "generated_plots": generated_plots,
    "plot_statistics": plot_statistics,
    "insights": insights
    }
    
def _validate_file(file: UploadFile):
    file_extension = Path(file.filename).suffix.lower()

    if file_extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Only CSV files are allowed."
        )
        
def _save_file(file: UploadFile):
    file_extension = Path(file.filename).suffix.lower()

    unique_filename = f"{uuid.uuid4()}{file_extension}"

    file_path = UPLOAD_DIR / unique_filename

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path, unique_filename

def _save_processed_file(df: pd.DataFrame, unique_filename: str):

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

    processed_file_path = PROCESSED_DIR / unique_filename

    df.to_csv(processed_file_path, index=False)

    return processed_file_path

def _read_csv(file_path: Path):
    try:
        df = pd.read_csv(file_path)
        return df

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the uploaded CSV file."
        )

def _build_metadata(
    df: pd.DataFrame,
    original_filename: str,
    stored_filename: str,
    analysis,
):
    return {
        "original_filename": original_filename,
        "stored_filename": stored_filename,
        "analysis": analysis,
    }