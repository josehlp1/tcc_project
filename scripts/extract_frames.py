import cv2
import os

# Configurações
input_folder = "data/raw_videos/"
output_folder = "data/frames/"
frame_rate = 5

os.makedirs(output_folder, exist_ok=True)

for video_file in os.listdir(input_folder):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(input_folder, video_file)
        cap = cv2.VideoCapture(video_path)

        frame_count = 0
        success, frame = cap.read()
        while success:
            if frame_count % frame_rate == 0:
                frame_filename = f"{video_file}_frame_{frame_count:04d}.jpg"
                cv2.imwrite(os.path.join(output_folder, frame_filename), frame)
            success, frame = cap.read()
            frame_count += 1

        cap.release()
print("✅ Frames extraídos com sucesso!")
