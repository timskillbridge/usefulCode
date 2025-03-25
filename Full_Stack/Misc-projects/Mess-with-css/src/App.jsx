import { useEffect, useState } from 'react'
import axios from 'axios'
import './App.css'

export default function App() {
  const [pokemon,setPokemon] = useState([]);
  const [formData,setFormData] = useState(null);
  const [pokeNum,setPokeNum] = useState(null);

  const getMon = async (num) => {
    const {data} = await axios.get(`https://pokeapi.co/api/v2/pokemon/${num}/`)
    setPokemon(data)
    console.log(data)
  }

  const handleClick = (e) => {
    e.preventDefault();
    setPokeNum(formData)
    setFormData("")

    }

  useEffect(() => {
    getMon(pokeNum)
  },[pokeNum])

  return (
    <>
  <div id='searchForm'>
    <form onSubmit={handleClick}>
      <input type="text"  value={formData} onChange={(e) =>setFormData(e.target.value)}/>
      <button type='submit'>Find</button>
    </form>
  </div>
  <div id="displayMon">
  {pokemon.sprites ? (
  <div id="imgContainer"  >
    <img src={pokemon.sprites.front_default} alt="Mon" />
  </div>
) : ""}
    {/* {pokemon?(
    <div id="imgContainer">
    <img src={pokemon.sprites.front_default} alt="Mon" />
    </div>):""} */}
  </div>
    </>
  )
}


