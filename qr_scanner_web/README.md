# Team QR Scanner for Quiz Events

A real-time QR code detection system for managing quiz team turns using Python backend + web frontend.

## Features

✅ **Real-time QR Scanning** - Scan QR codes from phone camera  
✅ **Live Leaderboard** - See which team raises their QR first  
✅ **7 Team Support** - Teams A through G  
✅ **Printable QR Codes** - Download all 7 QR codes as a ZIP file  
✅ **Timestamp Logging** - Know exactly when each team was detected  
✅ **Reset Capability** - Clear detections and start a new round  

## Project Structure

```
qr_scanner_web/
├── index.html          # Web frontend (camera + leaderboard)
├── backend.py          # FastAPI server (QR generation + detection logging)
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Installation & Setup

### 1. Install Dependencies

```bash
cd qr_scanner_web
pip install -r requirements.txt
```

### 2. Run the Backend Locally

```bash
python backend.py
```

The backend will start on `http://localhost:8000`

### 3. Open Frontend in Browser

Open `index.html` in your web browser (or serve it with a simple HTTP server)

```bash
# Option A: Using Python's built-in server
python -m http.server 8080

# Option B: Using Node.js http-server (if installed)
npx http-server .
```

Then navigate to `http://localhost:8080`

## How It Works

### Setup
1. Each team gets a printed QR code (download from "📥 Download QR Codes" button)
2. Place your phone in front of you to scan the codes

### During Quiz
1. Click "▶ Start Scanner" to activate the camera
2. Teams raise their QR codes
3. The scanner detects which team's code appears first
4. Leaderboard updates in real-time with detection order and timestamp
5. Click "🔄 Reset" to clear detections for a new round

### QR Code Format
Each QR code contains simple text: `TEAM_A`, `TEAM_B`, ... `TEAM_G`

## API Endpoints

### POST /api/detect
Log a team detection
```json
{
  "team": "TEAM_A",
  "timestamp": "14:30:45"
}
```

### GET /api/detections
Retrieve all detections in order

### GET /api/reset
Clear all detections

### GET /download-qr-codes
Download all 7 QR codes as ZIP file

### GET /generate-qr/{team}
Generate individual QR code (e.g., `/generate-qr/A`)

## Deployment to Vercel

### Step 1: Set Up Vercel API
The backend needs to run on a serverless function or dedicated server.

#### Option A: Deploy Backend to Vercel (via `/api` folder)
```bash
# Create api folder structure
mkdir api
cp backend.py api/
```

Edit `api/backend.py` to be compatible with Vercel serverless:

```python
from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

# ... (keep endpoints the same)

# For Vercel
from mangum import Mangum
handler = Mangum(app)
```

Then deploy:
```bash
vercel
```

#### Option B: Keep Backend on Local/Separate Server
- Keep backend running on your machine on port 8000
- Update frontend `API_BASE` constant to your server URL

### Step 2: Deploy Frontend to Vercel

```bash
vercel --name=qr-scanner
```

### Update API URL in Frontend
After deployment, update the `API_BASE` in `index.html`:
```javascript
const API_BASE = 'https://your-vercel-backend.vercel.app';
```

## Usage Examples

### Print QR Codes
1. Click "📥 Download QR Codes"
2. Extract the ZIP file
3. Print each PNG image (high quality)
4. Laminate for durability during event

### Test Scanner
Visit: `http://localhost:8000/generate-qr/A` to test QR generation

## Troubleshooting

**Camera not working?**
- Ensure you've granted camera permissions to the browser
- Use HTTPS (required for camera access in production)

**Backend connection error?**
- Check if backend is running on `localhost:8000`
- Verify CORS is enabled (it is by default)

**QR codes not scanning?**
- Ensure good lighting
- Hold codes steady in front of camera
- Check QR code size (shouldn't be too small)

## File Sizes & Optimization

- HTML: ~12KB (minified)
- QR Codes: ~2-3KB each (PNG)
- Total ZIP: ~20KB

## Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript (jsQR library)
- **Backend**: Python (FastAPI, Uvicorn)
- **QR Generation**: qrcode library with Pillow
- **Hosting**: Vercel (frontend) + Optional backend service

## Security Notes

- Camera feed is processed locally in browser (no upload)
- Detections are logged to backend with timestamps
- No authentication required (suitable for local event use)
- Add authentication if exposing to internet

## Future Enhancements

- [ ] Audio/visual feedback for detection
- [ ] Team score tracking
- [ ] Export results to CSV
- [ ] Mobile app version
- [ ] Bluetooth trigger detection
- [ ] Live streaming leaderboard

## License

Open source - Use freely for quiz events!

---

**Questions?** Check the code comments or feel free to modify for your needs!
