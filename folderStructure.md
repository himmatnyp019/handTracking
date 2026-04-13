hand-gesture/
│
├── gesture_env/                  # Virtual environment (auto-generated, don't touch)
│
├── src/                          # All source code lives here
│   ├── core/                     # Core detection engines
│   │   ├── __init__.py
│   │   ├── hand_tracker.py       # MediaPipe setup & landmark detection
│   │   ├── finger_counter.py     # Finger counting logic
│   │   └── gesture_detector.py   # Swipe, pinch, fist etc (Phase 2)
│   │
│   ├── gestures/                 # Each gesture as its own file (easy to study)
│   │   ├── __init__.py
│   │   ├── count_fingers.py      # ✅ Phase 1 — you are here
│   │   ├── swipe.py              # Phase 2
│   │   ├── pinch.py              # Phase 2
│   │   ├── fist.py               # Phase 2
│   │   └── point.py              # Phase 2
│   │
│   ├── display/                  # UI / what gets drawn on screen
│   │   ├── __init__.py
│   │   └── renderer.py           # cv2 drawing, text, overlays
│   │
│   └── utils/                    # Helper functions
│       ├── __init__.py
│       ├── landmark_helpers.py   # Distance, angle math between landmarks
│       └── camera.py             # Webcam open/close/config
│
├── tests/                        # Test each module independently
│   ├── test_finger_counter.py
│   └── test_gesture_detector.py
│
├── assets/                       # Images, reference diagrams
│   └── hand_landmarks.png        # MediaPipe 21-point diagram (save for reference)
│
├── notebooks/                    # Jupyter notebooks for experimenting
│   └── explore_landmarks.ipynb   # Print & visualize raw landmark data
│
├── bridge/                       # Phase 3 — Python ↔ React communication
│   ├── websocket_server.py       # Sends gesture events to React
│   └── event_mapper.py           # Maps gesture → action name
│
├── docs/                         # Your own notes
│   ├── gestures_plan.md          # What each gesture will do in React
│   └── progress.md               # Track what's done / what's next
│
├── main.py                       # 🚀 Entry point — runs everything
├── config.py                     # Camera index, confidence thresholds, colors
├── requirements.txt              # pip freeze > requirements.txt
└── README.md                     # Project description