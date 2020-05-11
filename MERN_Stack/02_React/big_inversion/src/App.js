import React from 'react';
import './App.css';
import PersonCard from './components/components';

function App() {
  return (
    <div className="App">
      <PersonCard firstName="Ted" lastName="Crisp" age={32} hairColor="Brown"></PersonCard>
      <PersonCard firstName="Jessica" lastName="Palmer" age={36} hairColor="Blonde"></PersonCard>
      <PersonCard firstName="Phil" lastName="Myman" age={39} hairColor="Brown"></PersonCard>
      <PersonCard firstName="Lem" lastName="Hewitt" age={44} hairColor="Black"></PersonCard>
    </div>
  );
}

export default App;
