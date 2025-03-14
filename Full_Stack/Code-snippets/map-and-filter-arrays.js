
// Map to iterate through
<ul>
{
  characters.map((item,index) => (
    <li key={index}>{item.name} index: {index}</li>
  ))
}
</ul>

// Filter to produce new array with or without specified value

//With
// Removing an item by index
setMyArray(prevArray => prevArray.filter((_, index) => index === indexToRemove));

// Removing an item by value
setMyArray(prevArray => prevArray.filter(item => item === itemToRemove));

//Without


// Removing an item by index
setMyArray(prevArray => prevArray.filter((_, index) => index !== indexToRemove));

// Removing an item by value
setMyArray(prevArray => prevArray.filter(item => item !== itemToRemove));