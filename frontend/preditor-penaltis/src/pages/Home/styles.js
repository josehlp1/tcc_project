import styled, { keyframes } from 'styled-components';

const rotate = keyframes`
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
`;

export const Container = styled.div`
  text-align: center;
  margin-top: -10vh;
`;

export const Title = styled.h1`
  margin-bottom: 32px;
  color: rgb(255, 255, 255);
  display: flex;
  flex-direction: column;
  align-items: center;

  i.rotating-icon {
    font-size: 7vw;
    margin-bottom: 50px;
    animation: ${rotate} 10s linear infinite;
  }
`;
