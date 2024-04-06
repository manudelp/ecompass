import { useState } from 'react';
import Header from './components/Header/Header';
import Home from './components/Home/Home';
import './App.css';

function App() {
  return (
    <>
      <Header />
      <Home name='John Doe' />
    </>
  )
}
    

export default App
