# 🎯 TEAM QR SCANNER - COMPLETE SETUP GUIDE

## 📋 What You Have

A production-ready **Real-time QR Code Scanner for Quiz Events** with:
- ✅ 7 Printable QR Codes (TEAM_A to TEAM_G)
- ✅ Web-based live scanner (camera + leaderboard)
- ✅ Python FastAPI backend (QR generation + logging)
- ✅ Ready-to-deploy Vercel configuration
- ✅ 100% functional, tested, and documented

---

## 🚀 GETTING STARTED (EASY)

### Option A: Windows (Recommended)
```bash
# Just double-click this file:
launcher.bat
```

### Option B: Manual (Any OS)

**Terminal 1 - Backend:**
```bash
cd qr_scanner_web
pip install -r requirements.txt
python backend.py
```

**Terminal 2 - Frontend:**
```bash
cd qr_scanner_web
python -m http.server 8080
```

**Browser:**
```
http://localhost:8080
```

---

## 📱 Using During Your Quiz Event

### Before the Event (Prep)
1. Open `http://localhost:8080` in your browser
2. Click **"📥 Download QR Codes"** button
3. Extract the ZIP file
4. Print all 7 PNG files (high quality, A4 or larger)
5. Optionally laminate them for durability

### During the Event (Quiz Round)
1. Give one QR code to each team (A through G)
2. Position your phone/tablet camera in front of teams
3. Click **"▶ Start Scanner"** button
4. Ask your quiz question
5. Say: **"Raise your QR code!"**
6. Scanner detects who raised first
7. **Leaderboard updates** with detection order and time
8. Read the #1 team to answer question
9. Click **"🔄 Reset"** button for next question
10. Repeat from step 3

### Features During Scanning
- **Real-time Detection**: QR codes detected in milliseconds
- **Accurate Ranking**: Shows exact order of detection
- **Timestamps**: Know precise timing of each detection
- **Visual Feedback**: Green border when team detected
- **Easy Reset**: Clear leaderboard for new round

---

## 📂 File Reference

### Core Files
| File | Purpose | Size |
|------|---------|------|
| `index.html` | Web interface (open in browser) | 12 KB |
| `backend.py` | FastAPI server (run with `python`) | 3 KB |
| `requirements.txt` | Python dependencies | < 1 KB |

### Support Files
| File | Purpose |
|------|---------|
| `generate_qr_codes.py` | Regenerate QR codes anytime |
| `launcher.bat` | Easy Windows launcher |
| `setup.bat` | Setup dependencies (Windows) |
| `vercel.json` | Deploy to Vercel (optional) |

### Documentation
| File | Content |
|------|---------|
| `README.md` | Complete technical documentation |
| `QUICKSTART.md` | Quick reference guide |
| `PROJECT_SUMMARY.md` | Project overview |
| `SETUP_GUIDE.md` | This file! |

### Generated Files
| File | Content |
|------|---------|
| `team_qr_codes.zip` | All 7 QR codes (ready to download) |
| `qr_codes_generated/` | Individual QR code PNG files |

---

## 🎯 The Flow Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    QUIZ EVENT HOST                          │
│                  (Your Computer/Phone)                      │
│                                                             │
│  Browser: http://localhost:8080                            │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ 🎯 Team QR Scanner                                  │  │
│  │                                                      │  │
│  │  ▶ Start Scanner  🔄 Reset  📥 Download QRs        │  │
│  │                                                      │  │
│  │  Camera Feed:        Leaderboard:                   │  │
│  │  ┌──────────┐       #1 TEAM_A  14:30:45           │  │
│  │  │          │       #2 TEAM_C  14:30:46           │  │
│  │  │  📹 QR  │       #3 TEAM_E  14:30:47           │  │
│  │  │ DETECTED │       #4 TEAM_B  14:30:49           │  │
│  │  │          │                                       │  │
│  │  └──────────┘                                       │  │
│  │                                                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                          ▲                                  │
│                          │ (Browser Camera)               │
│                          │                                │
└──────────────────────────┼────────────────────────────────┘
                          │
                          │
                  ┌───────▼────────┐
                  │   TEAMS       │
                  │               │
                  │ TEAM A: [QR]  │
                  │ TEAM B: [QR]  │
                  │ TEAM C: [QR]  │
                  │ ... (7 teams) │
                  │               │
                  └───────────────┘

Python Backend (Port 8000)
  ├─ POST /api/detect → logs team detection
  ├─ GET /api/detections → returns leaderboard
  ├─ GET /download-qr-codes → QR code ZIP
  └─ GET /api/reset → clears leaderboard
```

---

## 🔧 Troubleshooting

### Camera Not Working

**Problem**: "Camera access denied" or no camera feed
**Solution**:
1. Browser must ask for permission → Click **"Allow"**
2. Only works with **HTTPS** in production (HTTP OK locally)
3. Some privacy browsers (Brave, DuckDuckGo) block cameras → Use Chrome/Firefox
4. Make sure camera isn't already in use by another app

**Test**: 
- Go to: http://localhost:8080
- Click "▶ Start Scanner"
- You should see your camera feed

---

### QR Code Not Scanning

**Problem**: "Holder QR codes but scanner doesn't detect"
**Solution**:
1. **Lighting**: Ensure bright overhead/side lighting (no backlit QR)
2. **Distance**: Hold QR code 20-40cm from camera
3. **Stability**: Hold QR code still for 1-2 seconds
4. **Size**: Printed QR should be at least 10x10cm
5. **Angle**: Point camera directly at code (not at angle)

**Test Code**:
- Visit: `http://localhost:8000/generate-qr/A`
- Save the image and try scanning it

---

### Backend Not Starting

**Problem**: "Connection refused" or "Port 8000 in use"
**Solution**:
```bash
# Check what's using port 8000
lsof -i :8000  # macOS/Linux
netstat -ano | findstr :8000  # Windows

# Kill the process and try again
python backend.py
```

---

### Frontend Not Loading

**Problem**: "Cannot find http://localhost:8080"
**Solution**:
```bash
# Make sure you ran:
python -m http.server 8080

# Check it says:
# Serving HTTP on 0.0.0.0 port 8080

# Then open browser to:
http://localhost:8080
```

---

### "API_BASE not responding"

**Problem**: Status shows "Cannot connect to backend"
**Solution**:
1. Ensure backend is running: `python backend.py`
2. Check in browser console (F12) for error details
3. Verify `API_BASE` in `index.html` line 167

---

## 🌐 Deploying to Vercel (Optional)

### Why Deploy?
- Run from anywhere (not just your computer)
- No need to keep terminal open
- Accessible from multiple devices

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Deploy Frontend
```bash
cd qr_scanner_web
vercel --name=qr-scanner
```

### Step 3: Update Backend URL
Edit `index.html` line 167:
```javascript
// Change from:
const API_BASE = 'http://localhost:8000';

// To your backend URL (if deployed):
const API_BASE = 'https://your-backend-url.com';
```

### Step 4: Backend Options
Choose one:

**Option A**: Keep backend on your machine (local)
- Backend runs on `localhost:8000`
- Frontend runs on Vercel
- Works great for same-building events

**Option B**: Deploy backend too (cloud)
- Use Railway.app, Render.com, or Fly.io
- More complex, but works anywhere
- Recommended for remote events

---

## 📊 API Documentation

### POST /api/detect
**Detect a team**
```
URL: http://localhost:8000/api/detect
Method: POST
Body: {"team": "TEAM_A", "timestamp": "14:30:45"}

Response:
{
  "status": "detected",
  "team": "TEAM_A",
  "rank": 1
}
```

### GET /api/detections
**Get all detections**
```
URL: http://localhost:8000/api/detections
Method: GET

Response:
{
  "detections": [
    {"team": "TEAM_A", "timestamp": "14:30:45", "server_time": "2024-04-24..."},
    {"team": "TEAM_C", "timestamp": "14:30:46", "server_time": "2024-04-24..."}
  ]
}
```

### GET /api/reset
**Clear all detections**
```
URL: http://localhost:8000/api/reset
Method: GET

Response:
{"status": "reset"}
```

### GET /download-qr-codes
**Download all QR codes as ZIP**
```
URL: http://localhost:8000/download-qr-codes
Method: GET
Returns: ZIP file with all 7 QR codes
```

### GET /generate-qr/{team}
**Generate individual QR code**
```
URL: http://localhost:8000/generate-qr/A
Method: GET
Returns: PNG image (TEAM_A.png)
```

---

## ✨ Tips & Tricks

### Tip 1: Mount Camera on Stand
- Use phone/tablet stand to stabilize camera
- Better detection with steady camera

### Tip 2: Test Before Event
- Test with all 7 teams before actual event
- Check lighting and distance
- Verify all QR codes scan properly

### Tip 3: Backup QR Codes
- Keep digital copies of QR code images
- Easy to reprint if laminated ones wear out

### Tip 4: Use in Low Light
- Turn on phone flashlight/screen light
- Ensure QR code is well-lit
- Black & white codes work best

### Tip 5: Multiple Devices
- Run frontend on one device
- Backend can serve multiple devices
- Each device sees the same leaderboard

---

## 🎮 Practice Quiz Event Script

```
🟢 SETUP (5 min)
├─ Print all 7 QR codes
├─ Give one to each team
├─ Arrange teams in front of camera
└─ Do camera position test

🟡 ROUND 1 (5 min per question)
├─ Click "▶ Start Scanner"
├─ Ask question to all teams
├─ Say "Raise your QR code!"
├─ Wait 3-5 seconds for detection
├─ Read #1 team to answer
├─ Verify answer correctness
└─ Award points

🔵 REPEAT (for each question)
├─ Click "🔄 Reset"
├─ Ask next question
├─ Repeat scanning process
└─ Keep cumulative score

🟣 RESULTS (2 min)
├─ Count total points per team
├─ Announce winner
├─ Optional: Export detections log
└─ Celebrate! 🎉
```

---

## 📝 Customization Quick-Start

### Change Team Names (A-G → Custom Names)
Edit `backend.py` line 16:
```python
teams = ['Alpha', 'Bravo', 'Charlie', 'Delta', 'Echo', 'Foxtrot', 'Golf']
```

Then regenerate QR codes:
```bash
python generate_qr_codes.py
```

### Add More Teams (7 → 10)
Edit `backend.py` line 16:
```python
teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
```

### Change QR Code Size
Edit `generate_qr_codes.py` lines 12-13:
```python
box_size=15,  # Larger boxes
border=6,     # Larger border
```

---

## 🆘 Still Have Questions?

1. **Quick Questions** → Check `QUICKSTART.md`
2. **Technical Details** → Check `README.md`
3. **API Details** → Check `PROJECT_SUMMARY.md`
4. **Backend Code** → Read `backend.py` (well-commented)
5. **Frontend Code** → Read `index.html` (well-commented)

---

## ✅ Pre-Event Checklist

- [ ] Tested backend starts with: `python backend.py`
- [ ] Tested frontend loads: `http://localhost:8080`
- [ ] Downloaded and printed QR codes
- [ ] Tested camera permission works
- [ ] Tested QR scanning with test code
- [ ] Checked lighting is adequate
- [ ] Have backup copies of QR codes
- [ ] Tested with all 7 team codes
- [ ] Reset button works
- [ ] Ready to rock! 🎉

---

## 🎯 You're All Set!

Everything is configured and ready to use:

```bash
# Start backend (Terminal 1)
python backend.py

# Start frontend (Terminal 2)
python -m http.server 8080

# Open browser
http://localhost:8080

# Click "Start Scanner" and have fun! 🎉
```

**Enjoy your quiz event!**

---

*Questions? File is comprehensive and well-documented.*
*Issues? Backend API is stable and tested.*
*Ready? Let's go! 🚀*
