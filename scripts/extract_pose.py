import cv2
import mediapipe as mp
import json
import os

mp_pose = mp.solutions.pose
pose = mp_pose.Pose()

input_folder = "data/frames/"
output_folder = "data/keypoints/"
os.makedirs(output_folder, exist_ok=True)

for frame_file in os.listdir(input_folder):
    if frame_file.endswith(".jpg"):
        image_path = os.path.join(input_folder, frame_file)
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # Detectar pose
        results = pose.process(image_rgb)
        if results.pose_landmarks:
            landmarks = {f"point_{i}": [lm.x, lm.y] for i, lm in enumerate(results.pose_landmarks.landmark)}
            
            # Salvar dados
            output_path = os.path.join(output_folder, frame_file.replace(".jpg", ".json"))
            with open(output_path, "w") as f:
                json.dump(landmarks, f)

print("✅ Pose do jogador extraída com sucesso!")
