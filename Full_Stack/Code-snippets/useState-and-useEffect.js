//  Simple values
const [desiredState,setDesiredState] = useState(value)

//  Arrays

const [usedArray,setUsedArray] = useState([]) // - Null

// Arrays using a formula to set the initial value
const [mole,setMole] = useState(() => {
    const initialField = new Array(9).fill(false)
    return initialField});


//  useEffect runs when specificed useState value changes or every re-render

useEffect(() => {
    console.log("Example of a useEffect")
},['runs if variables in this array change'])

//   useEffect are ways to update useStates

const updateArrayValue = ((index,val) => {
    setArray((a) => {  //use the first letter of the array you're updating, this value is the most recent version in memory, not the useState
      const newArr = [...a]
      newArr[index] = val
      return newArr  //sets Array using setArray to the new value
    })
  })
