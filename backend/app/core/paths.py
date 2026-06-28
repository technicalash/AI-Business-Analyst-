from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[3]

UPLOAD_DIR = BASE_DIR / "backend" / "storage" / "uploads"

PROCESSED_DIR = BASE_DIR / "backend" / "storage" / "processed"
