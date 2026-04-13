# src/core/hand_tracker.py

import cv2
import mediapipe as mp
import config

class HandTracker:
    def __init__(self):
        # New MediaPipe API (0.10+)
        from mediapipe.tasks import python
        from mediapipe.tasks.python import vision

        self.mp_draw = mp.solutions.drawing_utils
        self.mp_hands = mp.solutions.hands
        self.hands = mp.solutions.hands.Hands(
            static_image_mode=False,
            max_num_hands=config.MAX_HANDS,
            min_detection_confidence=config.MIN_DETECTION_CONFIDENCE,
            min_tracking_confidence=config.MIN_TRACKING_CONFIDENCE
        )

    def find_hands(self, frame):
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = self.hands.process(rgb)

        landmarks_list = []

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame,
                    hand_landmarks,
                    self.mp_hands.HAND_CONNECTIONS
                )
                landmarks_list.append(hand_landmarks.landmark)

        return frame, landmarks_list