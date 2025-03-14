import { useState, useEffect } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import axios from 'axios'
import './App.css'

function App() {

    const getPokemonData = async (names) => {
      let promises = names.map((name) =>
        axios.get(`https://pokeapi.co/api/v2/pokemon/${name}`)
      );
      console.log(promises);
      let responses = await Promise.all(
        names.map((name) =>
          axios.get(`https://pokeapi.co/api/v2/pokemon/${name}`)
        )
      );
      console.log(responses);
    };

    useEffect(
      () => {
      getPokemonData(["ditto", "squirtle"]);
    },
    []
    );    


  return (
    <>

    </>
  )
}

export default App
