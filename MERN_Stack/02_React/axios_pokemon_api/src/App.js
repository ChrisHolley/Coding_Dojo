import React, { useEffect, useState } from 'react';
import './App.css';
import axios from 'axios';

function App() {
  const [pokemons, setPokemons] = useState([]);
  const [isClicked, setClicked] = useState(false);


  useEffect(() => {
    if (isClicked) {  
      axios.get("https://pokeapi.co/api/v2/pokemon/")
      .then(response => {
        setPokemons(response.data.results);
      })
    }
  }, [isClicked]);

  return (
    <div className="App">
      <button onClick={(e) => setClicked(true)}>Fetch Pokemon</button>
      <ul className="list-group">
        {pokemons.length > 0 && pokemons.map((pokemon, i) => {
          return (<li key={i} className="list-group-item">{pokemon.name}</li>)
        })}
      </ul>
    </div>
  );
}

export default App;
