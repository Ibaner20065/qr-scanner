from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from datetime import datetime
import qrcode
import zipfile
from pathlib import Path

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store detections with timestamps
detections = []
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

class Detection(BaseModel):
    team: str
    timestamp: str

@app.get("/", response_class=HTMLResponse)
async def root():
    """Serve the index.html file at root"""
    try:
        with open("index.html", "r") as f:
            return f.read()
    except FileNotFoundError:
        return """
        <html>
            <body style="font-family: Arial; padding: 20px;">
                <h1>QR Scanner</h1>
                <p>index.html not found. Please ensure index.html is in the root directory.</p>
            </body>
        </html>
        """

@app.post("/api/detect")
async def detect_team(detection: Detection):
    """Log team detection"""
    detections.append({
        "team": detection.team,
        "timestamp": detection.timestamp,
        "server_time": datetime.now().isoformat()
    })
    return {
        "status": "detected",
        "team": detection.team,
        "rank": len(detections)
    }

@app.get("/api/detections")
async def get_detections():
    """Get all detections in order"""
    return {"detections": detections}

@app.get("/api/reset")
async def reset_detections():
    """Clear all detections"""
    global detections
    detections = []
    return {"status": "reset"}

@app.get("/download-qr-codes")
async def download_qr_codes():
    """Generate and download all 7 QR codes as a ZIP file"""
    
    # Create a temporary directory for QR codes
    qr_dir = Path("qr_codes_temp")
    qr_dir.mkdir(exist_ok=True)
    
    # Generate QR codes for each team
    for team in teams:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(f"TEAM_{team}")
        qr.make(fit=True)
        
        img = qr.make_image(fill_color="black", back_color="white")
        qr_path = qr_dir / f"TEAM_{team}.png"
        img.save(qr_path)
    
    # Create ZIP file
    zip_path = "team_qr_codes.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for team in teams:
            qr_file = qr_dir / f"TEAM_{team}.png"
            zipf.write(qr_file, arcname=f"TEAM_{team}.png")
    
    # Clean up temporary directory
    for team in teams:
        (qr_dir / f"TEAM_{team}.png").unlink()
    qr_dir.rmdir()
    
    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="team_qr_codes.zip"
    )
