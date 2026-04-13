# src/display/renderer.py

import cv2
import config

def draw_finger_count(frame, count):
    """
    Draw the finger count number big on the screen.
    """
    cv2.putText(
        frame,
        str(count),
        config.COUNT_POSITION,
        config.FONT,
        config.COUNT_FONT_SCALE,
        config.COUNT_COLOR,
        config.COUNT_THICKNESS
    )
    return frame

def draw_info_bar(frame, count):
    """
    Draw a small info bar at the top showing finger count label.
    """
    label = f"Fingers: {count}"
    cv2.rectangle(frame, (0, 0), (300, 50), (0, 0, 0), -1)   # black bar
    cv2.putText(frame, label, (10, 35), config.FONT, 1, (255, 255, 255), 2)
    return frame