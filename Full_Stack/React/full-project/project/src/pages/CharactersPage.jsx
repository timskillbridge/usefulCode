
import React, {useState, useEffect } from 'react'
import axios from 'axios'
import { useNavigate } from 'react-router-dom';


export default function CharactersPage() {

// Step 1. useState to store data.

const [charData,setCharData] = useState([])

// Step 2. function to get characters (and log data in console)
const getCharacters = async () => {
  try {
    const {data} = await axios.get('https://thronesapi.com/api/v2/Characters');
    setCharData(data)
    // console.log(data)
  } catch (err) {
    alert(err);
  }
};

useEffect(() => {
  getCharacters();
},[])

const navigate = useNavigate()

const validateResponse = async (characterID) => {
  let {data, status} = await axios.get(`https://thronesapi.com/api/v2/Characters/${characterID}/`)
  if(status ==200){
    navigate(`/characters/${characterID}/`)
  }

  
}

  return (
    <>
    <div>CharactersPage</div>

    <ul>

    {charData.map((char, index) => (
      <li key={index} onClick={() => validateResponse(`${char.id}`)}>{char.fullName}</li>
    ))}

    </ul>


    </>
  )
}
