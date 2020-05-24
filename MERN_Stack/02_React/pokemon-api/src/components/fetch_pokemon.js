import React, { useState, useEffect } from 'react';


const FetchPokemon = (props) => {
    const [pokemon, setPokemon] = useState(0);

    useEffect(() => {
        console.log("useEffect running")
        fetch('https://pokeapi.co/api/v2/pokemon/')
            .then(response => response.json())
            .then(response => setPokemon({
                poke: response.results
            }))
    }, []);
    return(
        <div>
            {pokemon.poke ? pokemon.poke.map((item, index) => {
                return(<div key={index}>{item.name}</div>)
            }):null}
        </div>
    );
}
export default FetchPokemon;