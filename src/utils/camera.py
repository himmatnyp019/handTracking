# src/utils/camera.py

import cv2
import config

def open_camera():
    """
    Open webcam and set resolution.
    Returns cap object.
    """
    cap = cv2.VideoCapture(config.CAMERA_INDEX)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, config.CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, config.CAMERA_HEIGHT)

    if not cap.isOpened():
        raise RuntimeError("❌ Camera not found. Check CAMERA_INDEX in config.py")

    print("✅ Camera opened successfully")
    return cap

def read_frame(cap):
    """
    Read one frame. Returns (success, frame)
    """
    ret, frame = cap.read()
    if not ret:
        return False, None

    if config.FLIP_CAMERA:
        frame = cv2.flip(frame, 1)

    return True, frame

def close_camera(cap):
    cap.release()
    cv2.destroyAllWindows()
    print("📷 Camera closed")