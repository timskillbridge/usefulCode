
import React from 'react'
import { useOutletContext } from 'react-router-dom'

export default function CharCard({charData}) {
const {removeFavs, isFavorite, addToFavs, favorites} = useOutletContext()
   return (

    <>
    {charData.imageUrl?
    (
        <>
    <h1>{charData.fullName}</h1>
    <img src={charData.imageUrl} alt={charData.firstName} />
    <h2></h2>
    <ul>
        <li>
        {charData.family}
        </li>
        <li>
        {charData.title}
        </li>
    </ul>
    {isFavorite(charData)?
   (
    <button onClick={() => removeFavs(charData)}>Remove</button>
   )
   : <button onClick={() => addToFavs(charData)}>Add</button>
   
}
    </>
    ):'loading'}
    </>

  )
}
