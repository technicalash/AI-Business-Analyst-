from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.upload import router as upload_router
from app.api.download import router as download_router
from app.api.download_report import router as download_report_router
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload_router)
app.include_router(download_router)
app.include_router(download_report_router)

@app.get("/")
def home():
    return {
        "message":"App backend is running   !"
    }
    
app.mount("/storage", StaticFiles(directory="storage"), name="storage")
