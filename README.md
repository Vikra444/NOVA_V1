<h1 align="center">🌌 NOVA_V1</h1>
<h3 align="center">Advanced Desktop AI Assistant (JARVIS-Style)</h3>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg">
  <img src="https://img.shields.io/badge/AI-Assistant-green?logo=googleassistant">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen">
</p>

---

## 🚀 Introduction

**NOVA_V1** is an advanced, modular, desktop-based AI assistant inspired by **Iron Man’s JARVIS**.  
It combines **voice control, automation, memory, vision, web search, system control**, and dynamic AI responses into one powerful framework.

Designed for **real-world usage**, not just a chatbot.  
Runs **offline locally** with optional online features.

---

## ✨ Key Features

### 🎙️ Voice Assistant  
- Mic input + smart command recognition  
- Google search, email, weather  
- System control via voice  

### 🧠 Memory System  
- Long-term context storage  
- Mood tracking  
- Interaction logging  

### 👁️ Computer Vision  
- YOLOv8 object detection  
- Camera snapshots  
- Real-time frame reading  

### 🖥️ Full Desktop Automation  
- Keyboard/mouse automation  
- Window control (open/close/minimize)  
- File opener & app launcher  

### 🌐 Online Intelligence  
- YouTube music player  
- News fetcher  
- Weather & web automation  

### 🧩 Modular Architecture  
Clean & expandable folders:  
- `features/` → extra modules & mood logger  
- `NOVA_PIPELINE/` → main command pipeline  
- `tools/` → debug/testing utilities  

---

## 📂 Project Folder Structure

```text
NOVA_V1/
├── NOVA_PIPELINE/              # Jarvis-like core functions
├── features/                   # Mood logger, addons, permissions, etc.
├── tools/                      # Tests: Google, camera, YouTube
├── screenshots/                # UI screenshots
├── NOVA_gui.py                 # GUI launcher
├── agent.py                    # Main NOVA engine
├── NOVA_memory.py              # Memory engine
├── NOVA_screenshot.py          # Screenshot system
├── NOVA_system_monitor.py      # PC health monitor
├── NOVA_youtube_music.py       # YouTube music control
├── requirements.txt            # Python dependencies
└── yolov8n.pt                  # Vision model

1️⃣ Clone the repo
git clone https://github.com/Vikra444/NOVA_V1.git
cd NOVA_V1


2️⃣ Create venv
python -m venv .venv
.venv\Scripts\activate


3️⃣ Install dependencies
pip install -r requirements.txt


▶️ How to Run
🟦 Run main AI engine
python agent.py console



🟩 Run GUI version
python start_gui.py



🟨 Test standalone features
python tools/test_google_search.py
python tools/test_camera_access.py
python tools/test_youtube_play.py


🛣️ Roadmap (Upcoming Features)
Hinglish optimized voice mode
Personality engine (emotional + adaptive)
Plugin marketplace system
IoT / Home automation
Better GUI dashboard
AI memory timeline visualization
More computer vision tools


🤝 Contribution
Pull requests welcome!
Tips:
Keep code modular
Add comments
Avoid pushing large files or secrets

👨‍💻 Author
Vikram
Creator of NOVA — A powerful JARVIS-inspired desktop AI system.

---

### Ab tujhe kya karna hai (super simple):

1. GitHub pe jaa → `NOVA_V1` repo open kar  
2. `README.md` pe click kar  
3. Upar right side **✏️ (edit)** pe click  
4. Jo bhi abhi andar hai **sab delete** kar  
5. Upar jo maine full block diya hai **poora copy–paste** kar de  
6. Niche commit message likh de: `Update professional README`  
7. **Commit changes** button daba de  

Bas.  
Ab tera README **clean, professional, aur perfect formatted** dikh lega.  

Agar tu bole, next step me NOVA ka **logo + architecture diagram** bhi design kar dete hain 😎
::contentReference[oaicite:0]{index=0}
