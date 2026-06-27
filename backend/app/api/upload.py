from fastapi import APIRouter, UploadFile
from app.services.upload_services import process_uploaded_file

router=APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile):
    return process_uploaded_file(file)