# config.py

# Camera Settings
CAMERA_INDEX = 0          # 0 = default webcam
CAMERA_WIDTH = 1280
CAMERA_HEIGHT = 720
FLIP_CAMERA = True        # Mirror view (like a selfie camera)

# MediaPipe Settings
MAX_HANDS = 1
MIN_DETECTION_CONFIDENCE = 0.7
MIN_TRACKING_CONFIDENCE = 0.7

# Finger Landmark IDs
FINGERTIP_IDS = [8, 12, 16, 20]    # Index, Middle, Ring, Pinky tips
FINGERPIP_IDS = [6, 10, 14, 18]    # Their middle joints

# Display Settings
FONT = 1                            # cv2.FONT_HERSHEY_SIMPLEX
COUNT_FONT_SCALE = 10
COUNT_COLOR = (0, 255, 0)           # Green
COUNT_THICKNESS = 20
COUNT_POSITION = (250, 400)         # Where number appears on screen

LANDMARK_COLOR = (0, 255, 255)
CONNECTION_COLOR = (255, 255, 255)

# Window
WINDOW_NAME = "Hand Gesture - Finger Counter"
QUIT_KEY = ord('q')