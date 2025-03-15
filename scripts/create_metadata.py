import os
import pandas as pd

frames_dir = "data/frames/"
keypoints_dir = "data/keypoints/"
bbox_dir = "data/bounding_boxes/"
output_csv = "data/metadata.csv"

metadata = []

for frame_file in os.listdir(frames_dir):
    if not frame_file.endswith(".jpg"):
        continue

    frame_path = os.path.join(frames_dir, frame_file)
    pose_path = os.path.join(keypoints_dir, frame_file.replace(".jpg", ".json"))
    bbox_path = os.path.join(bbox_dir, frame_file.replace(".jpg", ".json"))

    if not os.path.exists(pose_path) or not os.path.exists(bbox_path):
        continue

    if "left" in frame_file.lower():
        direction = "left"
    elif "right" in frame_file.lower():
        direction = "right"
    elif "center" in frame_file.lower():
        direction = "center"
    else:
        direction = "unknown"

    video_name = frame_file.split("_frame")[0]
    if video_name.endswith("_other"):
        video_source = video_name.replace("_other", "")
    else:
        video_source = video_name

    metadata.append({
        "frame": frame_file,
        "direction": direction,
        "pose_path": pose_path,
        "objects_path": bbox_path,
        "video_source": video_source
    })

# Salvar no CSV
df = pd.DataFrame(metadata)
df.to_csv(output_csv, index=False)
print(f"✅ metadata.csv criado com {len(df)} registros.")
