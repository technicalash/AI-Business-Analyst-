from fastapi import APIRouter
from fastapi.responses import FileResponse
from pathlib import Path

router = APIRouter()

@router.get("/download-report/{filename}")
def download_report(filename: str):

    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    report_path = (
        BASE_DIR
        / "storage"
        / "reports"
        / filename
    )

    return FileResponse(
        path=str(report_path),
        filename="AI_Business_Analyst_Report.pdf",
        media_type="application/pdf"
    )