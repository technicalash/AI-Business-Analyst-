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

ALLOWED_EXTENSIONS = {".csv"}

# Base directory (backend/)
BASE_DIR = Path(__file__).resolve().parents[2]

# Upload directory
UPLOAD_DIR = BASE_DIR / "storage" / "uploads"
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


def process_uploaded_file(file : UploadFile):
    
    _validate_file(file)
    
    file_path, unique_filename = _save_file(file)
    df = _read_csv(file_path)
    df = clean_dataset(df)
    analysis = analyze_dataset(df)
    preprocessing_plan = generate_preprocessing_plan(analysis)
    df = execute_preprocessing_plan(df, preprocessing_plan)
    processed_file_path=_save_processed_file(df, unique_filename)
    return {
        "message": "Dataset uploaded and preprocessed successfully.",
    "processed_filename": unique_filename,
    "preprocessing_report": preprocessing_plan
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