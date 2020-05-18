import React, { useState } from 'react';
import './App.css';
import Content from './components/Contents';
import Tabs from './components/Tabs';

function App() {
  const [setIndex, setIndexState] = useState(0)
  const changeValue = (textIndex) => {
    setIndexState(textIndex)
  }
  const textArray = [
    "Thor",
    "Odin",
    "Loki"
  ]

  return (
    <div className="App">
      <Tabs changeValue={() => changeValue(0)} tabLabel="Tab 1" />
      <Tabs changeValue={() => changeValue(1)} tabLabel="Tab 2" />
      <Tabs changeValue={() => changeValue(2)} tabLabel="Tab 3" />
      <p><Content displayText={textArray[setIndex]} /></p>
      
    </div>
  );
}

export default App;
