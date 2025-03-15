import React from 'react';
import { Card } from './styles';

const VideoUploadCard = ({ setVideo, onUpload }) => (
  <Card className="card shadow-lg p-4">
    <label htmlFor="videoInput" className="form-label">
      <i className="fa-solid fa-video"></i> Selecione um vídeo:
    </label>
    <input
      type="file"
      id="videoInput"
      accept="video/*"
      className="form-control mb-3"
      onChange={(e) => setVideo(e.target.files[0])}
    />
    <button className="btn btn-success w-100" onClick={onUpload}>
      <i className="fa-solid fa-upload"></i> Enviar e Prever
    </button>
  </Card>
);

export default VideoUploadCard;
