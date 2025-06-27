import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Thời gian cuối mỗi hành động
last_action_time = 0
ACTION_DELAY = 0.5  # giây

def get_center(landmarks, indices):
    xs = [landmarks[i].x for i in indices]
    ys = [landmarks[i].y for i in indices]
    return np.mean(xs), np.mean(ys)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_rgb.flags.writeable = False
        results = pose.process(frame_rgb)

        frame_rgb.flags.writeable = True
        frame = cv2.cvtColor(frame_rgb, cv2.COLOR_RGB2BGR)

        current_time = time.time()

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            lm = results.pose_landmarks.landmark

            # Lấy trung tâm vai và hông
            shoulder_center_x, _ = get_center(lm, [11, 12])
            hip_center_x, _ = get_center(lm, [23, 24])
            dx = shoulder_center_x - hip_center_x

            # Kiểm tra đủ delay mới được thực hiện hành động
            if current_time - last_action_time >= ACTION_DELAY:
                # Nghiêng trái/phải
                if dx > 0.07:
                    pyautogui.press("left")
                    print("LEFT")
                    last_action_time = current_time
                elif dx < -0.07:
                    pyautogui.press("right")
                    print("RIGHT")
                    last_action_time = current_time

                # Jump
                left_hand_y = lm[15].y
                right_hand_y = lm[16].y
                nose_y = lm[0].y
                if left_hand_y < nose_y and right_hand_y < nose_y:
                    pyautogui.press("up")
                    print("JUMP")
                    last_action_time = current_time

                # Slide
                head_y = lm[0].y
                hip_y = (lm[23].y + lm[24].y) / 2
                if head_y - hip_y > -0.1:
                    pyautogui.press("down")
                    print("SLIDE")
                    last_action_time = current_time

        # Hiển thị hình ảnh
        cv2.imshow("Pose Subway", cv2.flip(frame, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
