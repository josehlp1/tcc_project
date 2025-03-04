import os
import pandas as pd

frames_folder = "data/frames/"
keypoints_folder = "data/keypoints/"
bounding_boxes_folder = "data/bounding_boxes/"
output_csv = "data/metadata.csv"

data = []

for frame_file in os.listdir(frames_folder):
    if frame_file.endswith(".jpg"):
        label = "center" if "center" in frame_file else "left" if "left" in frame_file else "right"
        data.append({"frame": frame_file, "direction": label})

df = pd.DataFrame(data)
df.to_csv(output_csv, index=False)
print("✅ Metadata CSV criado!")
