

import { useEffect, useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/vite.svg";
import axios from "axios";
import "./App.css";
import Button from "react-bootstrap/Button";
import Card from "react-bootstrap/Card";

function App() {
  const [count, setCount] = useState(0);
  const [pokeData, setPokeData] = useState(null);

  const getPokemon = async () => {
    try {
      let { data } = await axios.get(
        "https://pokeapi.co/api/v2/pokemon/charizard"
      );
      setPokeData(data);
    } catch (err) {
      setPokeData(null);
    }
  };

  useEffect(() => {
    console.log(pokeData);
  }, [pokeData]);

  useEffect(() => {
    getPokemon();
  }, []);

  return (
    <>
      <div>
        <a href="https://vitejs.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
      <h1>Farse</h1>
      <h1>Vite + React</h1>
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.jsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
      {pokeData ? (
        <Card style={{ width: "18rem" }}>
          <Card.Img variant="top" src={pokeData.sprites.front_default} />
          <Card.Body>
            <Card.Text>{pokeData.name}</Card.Text>
            <Button variant="primary">Go somewhere</Button>
          </Card.Body>
        </Card>
      ) : null}
    </>
  );
}

export default App;