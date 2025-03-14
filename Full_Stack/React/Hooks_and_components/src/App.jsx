import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import "./App.css";
import axios from 'axios'

function App() {
  // declare variable array, first variable is reference for value, second is function to update state with initial value
  const [pokemon, setPokemon] = useState("goldeen"); //This initial value values in the h3 tag below referencing the variable
                                                     // useState is the variable, not pokemon
  const [greeting, setGreeting] = useState("hey")
  const [pokemonData, setPokemonData] = useState(null)
//            getter         setter         init value

  const getPokemonInfo = async () => {
    // evt.preventDefault()
    let {data} = await axios.get(`https://pokeapi.co/api/v2/pokemon/${pokemon}/`)
  
    setPokemonData(data)
  }

  useEffect(() => {   //basically constant listeners, take array of things to keep track of.  repalce console.log to do other things
    console.log(pokemonData)
  }, [pokemonData])

  useEffect(() => {   //   two parameters: 1 the thing you want it to do, 2: what you need it to keep track of
    getPokemonInfo();
  }, []);  // blank, not trackking anything after the first run

  return (
    <>
      <h1>useState and useEffect</h1>
      {
        pokemonData ?
      <img src={pokemonData.sprites.front_default} alt="No Image" />
      :
      null
}
      <h2>{greeting}</h2>
      <button onClick = {() => setGreeting("bye")}>Change Greeting</button>
      <h3>{pokemon.toUpperCase()}</h3> 
      <form onSubmit={(event) => [event.preventDefault(),getPokemonInfo()]}>
      <input
      type="text"
      placeholder="pokemon"
      value ={pokemon}
      onChange = {(e) => setPokemon(e.target.value)}
      />
      </form>
    </>
  );
}

export default App;
