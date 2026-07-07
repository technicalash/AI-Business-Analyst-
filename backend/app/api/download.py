from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.core.paths import PROCESSED_DIR

router = APIRouter()

@router.get("/download/{filename}")
def download_file(filename: str):

    file_path = PROCESSED_DIR / filename

    return FileResponse(
        path=file_path,
        filename="cleaned_dataset.csv",
        media_type="text/csv"
    )