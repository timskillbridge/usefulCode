
1. in app.jsx:

import useOutletContext and build functions to add to favorites and remove from favorites
define a useState for favorites and build a function to check if the current char is
in the favorites useState.

const [favorites,setFavorites] = useState([])

const addToFavs = (char) => {
    if (!isFavorite(char)) {
        setFavs([...f,char])
    }
}

const removeFavs = (char) => {
    setFavs(favorites.filter((item) => item.id !== char.id))
}

const isFavorite = (char) => {
    if (favorites.filter((item) => item.id === char.id).length) {
        return true;
    } else {
        return false;
    }
};

2. update outlet to add context

    <Outlet context={{favorites,addToFavs,removeFavs,isFavorite}}/>

3. create CharCard element in components, pass charData as prop from ACharacter page.
    Passing as a prop once data is available
 
       {charData.fullName?
        <CharCard charData = {charData}/>
        :''
        }

    accepting it as a prop in CharCard

    export default function CharCard({charData}) {

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
    </>
    ):'loading'}
    </>

  )
}

4. Export context in App and import and define const for context variables within ACharacter
    in App:
    <Outlet context = {{removeFavs, isFavorite, addToFavs, favorites}}/>
    in ACharacter:
     const {removeFavs, isFavorite, addToFavs, favorites} = useOutletContext()

5. Add button wrapped in terniary statement to add or remove from favorites depending on
    whether the character is in the favorites array (use the isFavs function already made and passed)

    In the CharCard component after importing useOutletContext and declaring their use:
    {isFavorite(charData)?
   (
    <button onClick={() => removeFavs(charData)}>Remove</button>
   )
   : <button onClick={() => addToFavs(charData)}>Add</button>
   
    }
    </>
    :''

6. Build Favorites page consisting of a char card for each character in favorites.
    Use a map
    {favorites.map((char,index) => (
    <CharCard charData = {char}/>
    ))}