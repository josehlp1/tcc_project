from flask import Flask, request, jsonify, send_from_directory
import os
import uuid
import cv2
import numpy as np
import tensorflow as tf
from utils.pose_utils import extract_keypoints_from_frame

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/outputs'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

model = tf.keras.models.load_model('model/pose_model.h5')
LABELS = ['left', 'center', 'right']

@app.route('/predict-video', methods=['POST'])
def predict_video():
    if 'video' not in request.files:
        return jsonify({'error': 'No video uploaded'}), 400

    video_file = request.files['video']
    temp_filename = f"temp_{uuid.uuid4()}.mp4"
    video_file.save(temp_filename)

    cap = cv2.VideoCapture(temp_filename)
    frame_results = []
    frames = []
    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame.copy())
        keypoints = extract_keypoints_from_frame(frame)
        if keypoints is not None:
            prediction = model.predict(keypoints, verbose=0)
            predicted_label = LABELS[np.argmax(prediction)]
            confidence = float(np.max(prediction))

            frame_results.append({
                'frame': frame_count,
                'prediction': predicted_label,
                'confidence': confidence
            })

        frame_count += 1

    cap.release()
    os.remove(temp_filename)

    if not frame_results:
        return jsonify({'error': 'No pose detected in any frame'}), 400

    final_prediction = max(frame_results, key=lambda x: x['confidence'])
    best_frame_index = final_prediction['frame']
    best_frame = frames[best_frame_index]

    label = final_prediction['prediction'].upper()
    confidence = final_prediction['confidence']
    text = f'{label} ({confidence*100:.1f}%)'
    cv2.putText(best_frame, text, (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)

    image_filename = f"{uuid.uuid4()}.jpg"
    image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_filename)
    cv2.imwrite(image_path, best_frame)

    return jsonify({
        'total_frames': frame_count,
        'most_confident_prediction': final_prediction,
        'image_url': f"/static/outputs/{image_filename}",
        'all_predictions': frame_results
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
