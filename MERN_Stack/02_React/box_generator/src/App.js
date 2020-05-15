import React, { useState } from 'react';
import './App.css';
import Form from './components/Form';
import BoxGenerator from './components/BoxGenerator'

function App() {
  const [state, setState] = useState([

  
  ])

  return (
    <div className="App">
     <Form state={state} setState={setState} />
     <div className="BoxArea">
       {state.map((box, i) => (
         <BoxGenerator key={i} color={box.color} height={box.height} width={box.width} />
       ))}
     </div>
    </div>
  );
}

export default App;
