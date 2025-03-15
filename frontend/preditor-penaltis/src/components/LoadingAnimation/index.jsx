import React from 'react';
import { Player } from '@lottiefiles/react-lottie-player';
import { Wrapper, Text } from './styles';

const LoadingAnimation = () => (
  <Wrapper className="mt-4">
    <Player
      src="https://assets5.lottiefiles.com/packages/lf20_h1n9gr2l.json"
      background="transparent"
      speed={1}
      style={{ width: 200, height: 200 }}
      loop
      autoplay
    />
    <Text className="fw-bold">Analisando o vídeo... ⏳</Text>
  </Wrapper>
);

export default LoadingAnimation;
