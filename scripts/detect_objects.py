from ultralytics import YOLO
import cv2
import json
import os

# Carrega o modelo pré-treinado (YOLOv8n é leve e rápido)
model = YOLO("yolov8n.pt")

input_folder = "data/frames/"
output_folder = "data/bounding_boxes/"
os.makedirs(output_folder, exist_ok=True)

# Processar cada frame
for frame_file in os.listdir(input_folder):
    if frame_file.endswith(".jpg"):
        image_path = os.path.join(input_folder, frame_file)

        # Rodar a detecção com YOLO
        results = model(image_path)
        frame_boxes = []

        for result in results:
            for box, cls in zip(result.boxes.xyxy, result.boxes.cls):
                label = model.names[int(cls)]
                # Mantém apenas "person" (goleiro) e "sports ball" (bola)
                if label in ["person", "sports ball"]:
                    bbox = {
                        "label": label,
                        "bbox": box.tolist()  # [x1, y1, x2, y2]
                    }
                    frame_boxes.append(bbox)

        # Salvar as bounding boxes em JSON
        output_path = os.path.join(output_folder, frame_file.replace(".jpg", ".json"))
        with open(output_path, "w") as f:
            json.dump(frame_boxes, f)

print("✅ Detecção de bola e goleiro concluída!")
