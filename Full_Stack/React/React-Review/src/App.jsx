import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {

  const [testSet, setTestSet] = useState(new Set([]));
  const [count,setCount] = useState(1);
  const [clickStar,setClickStar] = useState(false);

  const onOff = () => {
    setClickStar(prevFlip => {
      const newFlip = !prevFlip;
      console.log(newFlip);
      return newFlip
    })
  };

  const updateSet = (val) => {
    setTestSet((prevSet) => {
      const newSet = new Set(prevSet);
      newSet.add(val);
      return newSet
    })
  }
  const updateCount = ((val) => {
    setCount(c => c+(10*(c/2).toFixed(2)))
    
  })

  useEffect(() => {
    updateSet(count)
  },[count])


  return (
    <>
    <h1>test</h1>

      <button className={"border-2"} onClick={updateCount}>{testSet}</button>
      <br />
      {testSet}
      <br />

      <div className={"container-div"}>
      <button onClick={onOff} className = {` ${clickStar?'top-goldStar':'top-Star'}`}></button>
      <button onClick={onOff} className = {` ${clickStar?'bottom-goldStar':'bottom-Star'}`}></button>
      </div>
      <br /><br />
      
    </>
  )
}

export default App
