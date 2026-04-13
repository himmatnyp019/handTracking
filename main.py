# main.py

import cv2
import config
from src.core.hand_tracker import HandTracker
from src.gestures.count_fingers import count_fingers
from src.display.renderer import draw_finger_count, draw_info_bar
from src.utils.camera import open_camera, read_frame, close_camera

def main():
    print("🚀 Starting Hand Gesture - Finger Counter")
    print("👋 Show fingers to the camera")
    print("Press Q to quit\n")

    cap = open_camera()
    tracker = HandTracker()

    while True:
        success, frame = read_frame(cap)
        if not success:
            print("❌ Failed to read frame")
            break

        # Detect hands & get landmarks
        frame, landmarks_list = tracker.find_hands(frame)

        # Count fingers from first detected hand
        count = 0
        if landmarks_list:
            count = count_fingers(landmarks_list[0])

        # Draw on screen
        frame = draw_finger_count(frame, count)
        frame = draw_info_bar(frame, count)

        cv2.imshow(config.WINDOW_NAME, frame)

        if cv2.waitKey(1) & 0xFF == config.QUIT_KEY:
            print("👋 Quit pressed")
            break

    close_camera(cap)

if __name__ == "__main__":
    main()