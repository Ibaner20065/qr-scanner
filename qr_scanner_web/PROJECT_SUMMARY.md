# 🎯 TEAM QR SCANNER - PROJECT SUMMARY

## ✅ What Has Been Built

A **complete real-time QR code detection system** for quiz events hosted on **Vercel** with a **Python backend**.

### Features Included:

✅ **7 Printable QR Codes** (TEAM_A through TEAM_G)  
✅ **Real-time Camera Scanner** (JavaScript-based QR detection)  
✅ **Live Leaderboard** (Updates as teams are detected)  
✅ **Timestamp Logging** (Know exactly when each team was detected)  
✅ **Python FastAPI Backend** (QR generation + detection logging)  
✅ **Download All QR Codes** (Single ZIP file with all 7 codes)  
✅ **Reset Functionality** (Clear leaderboard for new rounds)  
✅ **Responsive Design** (Works on phone, tablet, desktop)  

---

## 📦 Project Structure

```
qr_scanner_web/
├── index.html                 # Web frontend (12 KB)
├── backend.py                # FastAPI server (3.5 KB)
├── generate_qr_codes.py      # Standalone QR generator (3.2 KB)
├── requirements.txt           # Python dependencies
├── README.md                  # Full documentation
├── QUICKSTART.md             # Quick start guide
├── launcher.bat              # Easy launcher for Windows
├── vercel.json              # Vercel deployment config
├── team_qr_codes.zip        # Ready-to-download QR codes (27 KB)
└── qr_codes_generated/      # Individual QR code images
    ├── TEAM_A_PRINTABLE.png
    ├── TEAM_B_PRINTABLE.png
    ├── ... (7 total)
    └── TEAM_G_PRINTABLE.png
```

---

## 🎯 How It Works

### For Quiz Host:
1. **Print QR Codes** - Click "Download" button, extract ZIP, print all 7 codes
2. **Distribute to Teams** - Give one code to each team
3. **Start Scanner** - Click "Start Scanner" button
4. **Ask Question** - Teams raise their QR code
5. **View Results** - Leaderboard shows detection order in real-time

### Technical Flow:
```
Browser Camera Feed (Video)
    ↓
JavaScript QR Detection (jsQR library)
    ↓
Valid QR Found (TEAM_A, TEAM_B, etc)
    ↓
Send to Python Backend (POST /api/detect)
    ↓
Backend Logs Detection (Timestamp recorded)
    ↓
Update Frontend Leaderboard (Real-time)
```

---

## 🚀 Running Locally

### Quick Start (3 commands):

```bash
# Terminal 1: Backend
cd qr_scanner_web
python backend.py

# Terminal 2: Frontend  
cd qr_scanner_web
python -m http.server 8080
```

Then open: **http://localhost:8080**

### Even Easier (Windows):
```bash
# Just run this:
launcher.bat
```

---

## 🌐 Deploying to Vercel

### Option 1: Frontend on Vercel + Backend on Your Machine

```bash
# Just deploy the frontend
vercel --name=qr-scanner

# Update API_BASE in index.html to your backend URL
# Keep backend running on your machine
```

### Option 2: Full Vercel Deployment

Files are ready for deployment:
- `vercel.json` - Already configured
- `backend.py` - Python FastAPI compatible with Vercel serverless
- `index.html` - Static frontend

Just run: `vercel`

---

## 📊 QR Code Details

Each QR code contains simple text:
- **TEAM_A**
- **TEAM_B**
- ... (up to TEAM_G)

Format: PNG images with team labels, 300 DPI, high quality

### Print Settings:
- **Size**: A4 or larger recommended
- **Quality**: High/Best
- **Color**: Yes (black & white is fine)
- **Laminate**: Yes (for durability)

---

## 💻 Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | HTML5 + CSS3 + JavaScript |
| QR Detection | jsQR library |
| Backend | Python + FastAPI |
| Web Server | Uvicorn |
| QR Generation | qrcode + Pillow |
| Hosting | Vercel (frontend) |
| Package Manager | pip |

---

## 📋 API Endpoints

```
POST /api/detect
  Detect a team
  Body: {team: "TEAM_A", timestamp: "14:30:45"}
  Returns: {status: "detected", team: "TEAM_A", rank: 1}

GET /api/detections
  Get all detections
  Returns: {detections: [...]}

GET /api/reset
  Clear all detections
  Returns: {status: "reset"}

GET /download-qr-codes
  Download all 7 QR codes as ZIP

GET /generate-qr/{team}
  Get individual QR code (e.g., /generate-qr/A)
```

---

## 📁 File Sizes

- HTML Frontend: 12 KB
- Backend Python: 3.5 KB
- QR Generator: 3.2 KB
- Each QR Code: ~4-5 KB
- All QR Codes ZIP: 27 KB
- Total: < 50 KB

---

## 🎮 How to Use During Event

### Setup (5 minutes)
1. Print all 7 QR codes
2. Give one to each team
3. Position your phone/camera

### Quiz (per round)
1. Click "Start Scanner" (or refresh for new round)
2. Ask question to teams
3. Say "Raise your QR code!"
4. Scanner detects who was first
5. Leaderboard shows ranking
6. Click "Reset" for next question

### Results
- Leaderboard shows detection order
- Timestamps recorded
- Can be exported via backend logs

---

## 🔧 Customization

### Change Team Names:
Edit `backend.py` line 16:
```python
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
```

### Change QR Code Size:
Edit `generate_qr_codes.py` lines 12-13:
```python
box_size=10,  # Size of each box
border=4,      # Border width
```

### Add Audio Alerts:
Add to `index.html` in `handleDetection()`:
```javascript
new Audio('beep.mp3').play();
```

---

## ✨ Key Advantages

1. **Real-time** - Instant detection with timestamps
2. **Fair** - No network delays, local processing
3. **Easy Setup** - Works on any device with camera
4. **Printable** - All QR codes ready to download
5. **Scalable** - Works for 7 teams, easily expandable
6. **Secure** - Camera data stays local
7. **Deployable** - Ready for Vercel hosting

---

## 📝 Next Steps

1. **Test Locally**
   ```bash
   python backend.py  # Terminal 1
   python -m http.server 8080  # Terminal 2
   # Visit http://localhost:8080
   ```

2. **Print QR Codes**
   - Click "📥 Download QR Codes"
   - Extract and print

3. **Deploy to Vercel** (Optional)
   ```bash
   vercel
   ```

4. **Run Quiz Event**
   - Start scanner
   - Teams raise QR codes
   - See results in real-time

---

## 🆘 Support Files

- **README.md** - Full documentation
- **QUICKSTART.md** - Quick start guide
- **launcher.bat** - Easy Windows launcher
- **generate_qr_codes.py** - Regenerate QR codes anytime

---

## 🎉 You're All Set!

Everything is ready to use. Just:
1. Run the backend: `python backend.py`
2. Run the frontend: `python -m http.server 8080`
3. Open: `http://localhost:8080`
4. Start scanning!

**Enjoy your quiz event! 🎯**

---

*Built with ❤️ for seamless team detection*
