
// Updating simple Data Types:

import { styleText } from "util";

//String  - Prepends 'New:' to the old value
const prependMessage = () => {
  styleText( prevText => {
    const newText = 'New: ' + prevText;
    console.log(newText);
    return newText
  })
};

// Updating Boolean - (flips the value)
const onOff = () => {
  setflip(prevFlip => {
    const newFlip = !prevFlip;
    console.log(newFlip);
    return newFlip
  })
};

// ------------------------------updating sets!
 const [testSet, setTestSet] = useState(new Set([]));
 
 const updateSet = (val) => {
  setTestSet((prevSet) => {
    const newSet = new Set(prevSet);
    newSet.add(val);
    return newSet
  })}

// ------------------------------updating arrays
// Adding an item to the array
setMyArray(prevArray => [...prevArray, newItem]);

// Removing an item by index
setMyArray(prevArray => prevArray.filter((_, index) => index !== indexToRemove));

// Removing an item by value
setMyArray(prevArray => prevArray.filter(item => item !== itemToRemove));

// Updating an item at a specific index
setMyArray(prevArray => 
  prevArray.map((item, index) => 
    index === indexToUpdate ? updatedItem : item
 ));

// Updating an item by condition
setMyArray(prevArray => 
  prevArray.map(item => 
    item.id === itemId ? { ...item, ...updatedProperties } : item
));

// To insert an item at a specific index
setMyArray(prevArray => [
    ...prevArray.slice(0, indexToInsert),
    newItem,
    ...prevArray.slice(indexToInsert)
  ]);

//build the function to re-use inserting item at specific index
  const insertItemAtIndex = (newItem, index) => {
    setMyArray(prevArray => [
      ...prevArray.slice(0, index),
      newItem,
      ...prevArray.slice(index)
    ]);
  };  
  // Usage
  insertItemAtIndex('new item', 2);


//--------------------------------updating objects
// Initial state setup
const [myObject, setMyObject] = useState({});

// Adding or updating a key-value pair
setMyObject(prevObject => ({
  ...prevObject,
  [newKey]: newValue
}));

// Removing a key
setMyObject(prevObject => {
  const newObject = { ...prevObject };
  delete newObject[keyToRemove];
  return newObject;
});

// Alternative way to remove a key (using destructuring)
setMyObject(prevObject => {
  const { [keyToRemove]: removed, ...rest } = prevObject;
  return rest;
});

// Updating a nested value
setMyObject(prevObject => ({
  ...prevObject,
  nestedObject: {
    ...prevObject.nestedObject,
    nestedKey: newValue
  }
}));

// Conditionally updating a value
setMyObject(prevObject => ({
  ...prevObject,
  [key]: someCondition ? newValue : prevObject[key]
}));

// Updating multiple keys at once
setMyObject(prevObject => ({
  ...prevObject,
  key1: value1,
  key2: value2
}));
