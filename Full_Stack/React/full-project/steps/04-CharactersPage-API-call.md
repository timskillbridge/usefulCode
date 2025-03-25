
Use the Game of Thrones API to get character data for the characters page

1. import useState with useEffect into the page and create a useState to store the array that will be called
    import axios as well for step 2

    import React, {useState, useEffect } from 'react'
    import axios from 'axios'
    
    const [charData,setCharData] = useState([])

2. create async function to do API call:

    const getCharacters = async () => {
    try {
        const {data} = await axios.get('https://thronesapi.com/api/v2/Characters');
        setCharData(data)
    } catch (err) {
        alert(err);
    }
    };

3. useEffect to trigger the getCharacters function upon loading

    useEffect(() => {
    getCharacters();
    },[])

4. in the return space, map through the charData array

    return (
    <>
    <div>CharactersPage</div>

    <ul>

    {charData.map((char) => (
      <li>{char.fullName}</li>
    ))}

    </ul>


    </>
  )