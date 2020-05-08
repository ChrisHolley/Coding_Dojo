import React from 'react';
import './App.css';
import PersonCard from './components/component'

function App() {
  return (
    <div className="App">
      <PersonCard firstName="Ted" lastName="Crisp" age="31" hairColor="Brown"/>
      <PersonCard firstName="Veronica" lastName="Palmer" age="35" hairColor="Blonde"/>
      <PersonCard firstName="Linda" lastName="Zwordling" age="29" hairColor="Blonde"/>
      <PersonCard firstName="Phil" lastName="Myman" age="41" hairColor="Black"/>
      <PersonCard firstName="Lem" lastName="Hewitt" age="38" hairColor="Black"/>
    </div>
  );
}

export default App;
// Create a component called PersonCard that accepts the following props: 

// firstName
// lastName
// age
// hairColor