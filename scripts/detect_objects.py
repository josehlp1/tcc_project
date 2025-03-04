from ultralytics import YOLO
import cv2
import json
import os

# Carregar modelo YOLO pré-treinado
model = YOLO("yolov8n.pt")

input_folder = "data/frames/"
output_folder = "data/bounding_boxes/"
os.makedirs(output_folder, exist_ok=True)

for frame_file in os.listdir(input_folder):
    if frame_file.endswith(".jpg"):
        image_path = os.path.join(input_folder, frame_file)

        # Rodar detecção
        results = model(image_path)

        # Salvar bounding boxes
        bounding_boxes = []
        for result in results:
            for box in result.boxes.xyxy:
                bounding_boxes.append(box.tolist())

        # Salvar JSON com bounding boxes
        output_path = os.path.join(output_folder, frame_file.replace(".jpg", ".json"))
        with open(output_path, "w") as f:
            json.dump(bounding_boxes, f)

print("✅ Detecção de bola e goleiro concluída!")
