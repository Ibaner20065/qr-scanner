# 🎯 Quick Start Guide - Team QR Scanner

## What You Built
A **real-time QR code detection system** for quiz events where:
- 7 printable QR codes (TEAM_A through TEAM_G)
- Web-based scanner that detects which team raises their QR first
- Live leaderboard showing detection order
- Python backend for QR generation + logging

---

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
cd qr_scanner_web
pip install -r requirements.txt
```

### Step 2: Run Backend (Terminal 1)
```bash
python backend.py
```
You should see:
```
INFO:     Application startup complete
```

### Step 3: Run Frontend (Terminal 2)
```bash
python -m http.server 8080
```

Then open browser: **http://localhost:8080**

---

## 📱 Using During Quiz

1. **Print QR Codes**
   - Click "📥 Download QR Codes" on the web page
   - Extract the ZIP file
   - Print each PNG (high quality recommended)
   - Give one to each team

2. **Start Scanning**
   - Click "▶ Start Scanner"
   - Allow camera permission
   - Teams raise their QR codes
   - Scanner detects and logs in order

3. **View Results**
   - Live leaderboard updates
   - Shows rank, team, and exact time
   - Click "🔄 Reset" for next round

---

## 📁 File Reference

| File | Purpose |
|------|---------|
| `index.html` | Web interface (camera + leaderboard) |
| `backend.py` | FastAPI server (QR generation, logging) |
| `generate_qr_codes.py` | Standalone QR generator |
| `requirements.txt` | Python dependencies |
| `team_qr_codes.zip` | Printable QR codes (ready to print) |

---

## 🌐 Deploy to Vercel

### Option A: Frontend Only (Backend on Local Machine)

1. Install Vercel CLI:
   ```bash
   npm install -g vercel
   ```

2. Deploy frontend:
   ```bash
   vercel --name=qr-scanner
   ```

3. Update `index.html`:
   - Change `API_BASE = 'http://localhost:8000'` to your backend URL

### Option B: Deploy Both (More Complex)

Need to use a Python hosting service like:
- Railway.app
- Render.com
- Fly.io
- Or keep backend on your machine

---

## 🔧 Troubleshooting

**Camera not working?**
- ✅ Browser asks for camera permission
- ✅ Using Chrome/Firefox (some privacy browsers block this)
- ✅ Using HTTPS in production

**QR codes not scanning?**
- ✅ Good lighting
- ✅ Hold code steady
- ✅ Code should be ~20-30cm from camera

**Backend connection error?**
- ✅ Backend running on `localhost:8000`
- ✅ Firewall isn't blocking port 8000

**Need different team names?**
- Edit line 16 in `backend.py`: `teams = ['A', 'B', 'C', 'D', 'E', 'F', 'G']`
- Run `generate_qr_codes.py` again

---

## 📊 What Happens Behind the Scenes

1. **Camera Feed**: Browser captures video from device camera
2. **QR Detection**: JavaScript library scans each frame for QR codes
3. **Backend Logging**: When detected, team data sent to Python backend
4. **Leaderboard**: Frontend displays detections in order with timestamps

---

## 🎨 Customization Ideas

- **Change Team Names**: Edit `backend.py` line 16
- **Different Timing**: Modify detection cooldown in `index.html`
- **Sound Alerts**: Add beep on detection
- **Export Results**: Add CSV download button
- **Mobile App**: Convert to React Native

---

## 📝 API Endpoints (for advanced use)

```
POST /api/detect
  {team: "TEAM_A", timestamp: "14:30:45"}

GET /api/detections
  Returns all detections in order

GET /api/reset
  Clears all detections

GET /download-qr-codes
  Returns ZIP of all QR codes

GET /generate-qr/{team}
  Individual QR code image
```

---

## 🎯 Example Event Flow

```
1. Team Setup (5 min)
   ├─ Print QR codes
   ├─ Give one to each team
   └─ Gather in front of camera

2. Quiz Round 1 (10 min)
   ├─ Click "Start Scanner"
   ├─ Ask question
   ├─ Teams raise QR codes
   ├─ Leaderboard updates
   └─ Note who was first

3. Quiz Round 2+ (repeat)
   ├─ Click "Reset"
   ├─ Ask next question
   ├─ Repeat scanning
   └─ Keep cumulative score
```

---

## 💡 Pro Tips

- **Lighting**: Best with overhead or side lighting (avoid backlight)
- **Distance**: 30-40cm from camera works best
- **Stability**: Mount phone/camera on stand for better detection
- **Lamination**: Laminate codes to prevent wear during events
- **Backup**: Keep digital copies of QR code images

---

## 🆘 Need Help?

1. Check the `README.md` for detailed documentation
2. Review `backend.py` comments for API details
3. Test individual QR code at: `http://localhost:8000/generate-qr/A`
4. Check browser console (F12) for JavaScript errors

---

**Happy Quiz Event! 🎉**

Questions? Start the backend and frontend, then visit http://localhost:8080
