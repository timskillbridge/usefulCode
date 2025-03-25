import { useState } from 'preact/hooks'
import './app.css'
import NavBar from './components/NavBar'
import { Outlet, useOutletContext } from 'react-router-dom'

export function App() {

  const [favorites,setFavorites] = useState([])

const addToFavs = (char) => {
    if (!isFavorite(char)) {
        setFavorites([...favorites,char])
    }
}

const removeFavs = (char) => {
    setFavorites(favorites.filter((item) => item.id !== char.id))
}

const isFavorite = (char) => {
    if (favorites.filter((item) => item.id === char.id).length) {
        return true;
    } else {
        return false;
    }
};


  return (
    <>
    <NavBar />
    <Outlet context = {{removeFavs, isFavorite, addToFavs, favorites}}/>
    </>
  )
}

export default App