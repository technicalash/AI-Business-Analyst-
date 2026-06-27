from pathlib import Path
import shutil
import uuid
import pandas as pd

from fastapi import UploadFile, HTTPException

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
    return _build_response(
        df,
        file.filename,
        unique_filename
    )
    
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

def _read_csv(file_path: Path):
    try:
        df = pd.read_csv(file_path)
        return df

    except Exception:
        raise HTTPException(
            status_code=400,
            detail="Unable to read the uploaded CSV file."
        )

def _build_response(
    df: pd.DataFrame,
    original_filename: str,
    stored_filename: str
):
    return {
        "original_filename": original_filename,
        "stored_filename": stored_filename,
        "rows": len(df),
        "columns": len(df.columns),
        "column_names": df.columns.tolist()
    }