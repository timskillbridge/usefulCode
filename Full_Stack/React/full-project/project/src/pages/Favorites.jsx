
import React from 'react'
import { useState, useEffect } from 'preact/hooks'
import { useOutletContext, useParams } from 'react-router-dom'
import axios from 'axios'
import CharCard from '../components/CharCard';

export default function Favorites() {
const {removeFavs, isFavorite, addToFavs, favorites} = useOutletContext()

  return (
    <>
        <div>Favorites</div>
{favorites.map((char,index) => (
    <CharCard charData = {char}/>
))}


  
  </>
  )
}
