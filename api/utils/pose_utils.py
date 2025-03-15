import mediapipe as mp
import numpy as np
import cv2

mp_pose = mp.solutions.pose

def extract_keypoints_from_frame(frame):
    with mp_pose.Pose(static_image_mode=False) as pose:
        results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

        if not results.pose_landmarks:
            return None

        keypoints = []
        for i in range(33):
            lm = results.pose_landmarks.landmark[i]
            keypoints.extend([lm.x, lm.y])

        return np.array(keypoints).reshape(1, -1)
