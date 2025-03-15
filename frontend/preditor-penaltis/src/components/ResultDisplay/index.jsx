import React from 'react';
import { ResultContainer } from './styles';

const ResultDisplay = ({ result }) => {
  if (result.error) {
    return (
      <div className="alert alert-danger mt-4" role="alert">
        <i className="fa-solid fa-exclamation-triangle"></i> <strong>Erro:</strong> {result.error}
      </div>
    );
  }

  const { most_confident_prediction, image_url } = result;

  return (
    <ResultContainer className="mt-4">
      <div className="alert alert-success text-start" role="alert">
        <i className="fa-solid fa-crosshairs"></i> <strong>Predição mais confiável:</strong>{' '}
        {most_confident_prediction.prediction.toUpperCase()} <br />
        <i className="fa-solid fa-magnifying-glass"></i> <strong>Confiança:</strong>{' '}
        {(most_confident_prediction.confidence * 100).toFixed(2)}%
      </div>

      <div className="mt-3 text-start">
        <h5>
          <i className="fa-solid fa-image"></i> Frame com maior confiança:
        </h5>
        <img
          src={image_url}
          className="img-fluid rounded border"
          style={{ maxHeight: '400px' }}
          alt="Frame com maior confiança"
        />
      </div>
    </ResultContainer>
  );
};

export default ResultDisplay;
