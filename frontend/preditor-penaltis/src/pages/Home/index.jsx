import React, { useState } from 'react';
import { Container, Title } from './styles';
import VideoUploadCard from '../../components/VideoUploadCard';
import LoadingAnimation from '../../components/LoadingAnimation';
import ResultDisplay from '../../components/ResultDisplay';
import toastr from 'toastr';

const Home = () => {
  const [video, setVideo] = useState(null);
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleUpload = async () => {
    if (!video) {
      toastr.warning('⚠️ Selecione um vídeo primeiro!', 'Atenção');
      return;
    }

    const formData = new FormData();
    formData.append('video', video);

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch('http://localhost:5001/predict-video', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) throw new Error('Erro ao processar vídeo');

      const data = await response.json();
      setResult(data);
      toastr.success('✅ Previsão concluída com sucesso!', 'Sucesso');
    } catch (err) {
      toastr.error('❌ Erro ao processar o vídeo!', 'Erro');
      setResult({ error: err.message });
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container>
      <Title>
        <i className="fa-solid fa-circle-nodes rotating-icon"></i>
        Preditor de Direção de Pênaltis
      </Title>

      <VideoUploadCard setVideo={setVideo} onUpload={handleUpload} />
      {loading && <LoadingAnimation />}
      {result && <ResultDisplay result={result} />}
    </Container>
  );
};

export default Home;
