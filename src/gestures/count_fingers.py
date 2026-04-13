# src/gestures/count_fingers.py

import config

def count_fingers(landmarks):
    """
    Count how many fingers are raised.
    landmarks = list of 21 MediaPipe landmark points for one hand
    Returns: int (0 to 5)
    """
    if not landmarks:
        return 0

    count = 0

    # --- Index, Middle, Ring, Pinky ---
    # Tip y < PIP y means finger is UP (lower y = higher on screen)
    for tip_id, pip_id in zip(config.FINGERTIP_IDS, config.FINGERPIP_IDS):
        if landmarks[tip_id].y < landmarks[pip_id].y:
            count += 1

    # --- Thumb (uses x-axis) ---
    # Tip x < joint 3 x means thumb is open to the left (mirrored camera)
    if landmarks[4].x < landmarks[3].x:
        count += 1

    return count