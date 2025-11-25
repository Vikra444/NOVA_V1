# NOVA_V1 🌌  
**An advanced desktop AI assistant framework inspired by JARVIS – with memory, vision, mood tracking, and full PC automation.**

![NOVA_V1 Banner](screenshots/2025-10-18_16-39-27.png)

> NOVA_V1 is a modular AI assistant that runs on your local machine and connects different abilities like voice control, web search, system monitoring, camera vision, and task automation into one unified “NOVA” brain.

---

## ✨ Core Capabilities

- 🎙️ **Voice Interaction**
  - Talk to NOVA using a microphone.
  - NOVA responds using TTS.
  - Can open apps, search Google, control windows, take screenshots, and more.

- 🧠 **Memory & Context**
  - Persistent memory storage (`NOVA_memory.py`).
  - Mood logging and context tracking.
  - Can be extended into a personal knowledge base.

- 👁️ **Computer Vision**
  - Object detection with `yolov8n.pt`.
  - Camera tests and snapshots.
  - Hooks for building higher-level vision features.

- 🖥️ **Desktop Control & Automation**
  - Keyboard and mouse automation (`keyboard_mouse_CTRL.py`).
  - Window management (`NOVA_window_CTRL.py`, `Jarvis_window_CTRL.py` in `NOVA_PIPELINE/`).
  - Ideal for building a “personal OS-level AI”.

- 🌐 **Online Intelligence**
  - Google search (`NOVA_google_search.py`).
  - News fetcher (`NOVA_news.py`).
  - Weather helper (`NOVA_get_whether.py`, `NOVA_PIPELINE/jarvis_get_whether.py`).
  - Email helper (`NOVA_email.py`).

- 🖼️ **Screen & Screenshot Tools**
  - Screenshot capture (`NOVA_screenshot.py`).
  - Screen logging utilities under `features/addons/`.

- 🎵 **Media Control**
  - YouTube / music integration (`NOVA_youtube_music.py`).
  - Test tools under `tools/`.

- 🧩 **Modular Feature System**
  - `features/` folder contains:
    - `addons/` → reminders, ambient sound detector, face registry, screen logger, etc.
    - `mood_logger/` → mood tracking with templates.
    - `permissions/` → basic visibility / safety layer.
    - `sample_feature/` → template for new functionality.

---

## 🧱 Project Structure (Overview)

```text
NOVA_V1/
├── NOVA_PIPELINE/              # Core Jarvis-style pipeline utilities
├── features/                   # Camera, mood logger, permissions, addons, etc.
├── tools/                      # Test scripts and utilities
├── kivy_mobile/                # Kivy config for mobile experiments
├── screenshots/                # UI / feature screenshots
├── NOVA_code_assistant.py      # Code helper / dev assistant
├── NOVA_email.py               # Email automation
├── NOVA_gui.py                 # GUI launcher
├── NOVA_memory.py              # Memory / logging system
├── NOVA_news.py                # News integration
├── NOVA_prompts.py             # Prompt templates for NOVA
├── NOVA_system_monitor.py      # System resource monitoring
├── NOVA_tasker_controller.py   # Task/control orchestration
├── NOVA_youtube_music.py       # YouTube/music logic
├── agent.py                    # Main NOVA agent entry point
├── start_gui.py                # Alternative GUI entry
├── requirements.txt            # Python dependencies
├── yolov8n.pt                  # YOLOv8 model (object detection)
└── .permissions.json           # Permission configuration
