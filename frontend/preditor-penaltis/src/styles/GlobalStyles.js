import { createGlobalStyle } from 'styled-components';

const GlobalStyles = createGlobalStyle`
  body {
    font-family: 'Roboto' ,sans-serif;
    background: #3c3c3c;
    min-height: 100vh;
    display: flex;
    align-items: center;
    justify-content: center;
  }
`;

export default GlobalStyles;
