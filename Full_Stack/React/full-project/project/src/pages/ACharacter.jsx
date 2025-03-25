
import React from 'react'
import { useState, useEffect } from 'preact/hooks'
import { useOutletContext, useParams } from 'react-router-dom'
import axios from 'axios'
import CharCard from '../components/CharCard';
import App from '../app';

export default function ACharacter() {

    const {characterID} = useParams();
    const [charData, setCharData] = useState([])
    const {removeFavs, isFavorite, addToFavs, favorites} = useOutletContext()

    const getChar = async () => {
    let {data, status} = await axios.get(`https://thronesapi.com/api/v2/Characters/${characterID}/`)
    setCharData(data)
    console.log(data)
    }

    useEffect(() => {
    getChar()
    },[])
  return (

    <>
   {charData.fullName?
   <>
   <CharCard charData = {charData}/>
   
   </>
   :''
}
    </>

  )
}
