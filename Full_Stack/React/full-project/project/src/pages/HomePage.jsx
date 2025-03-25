
import React from 'react'
import { useState, useEffect } from 'react'



export default function HomePage() {
  const lorem = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Ut rerum quisquam reiciendis, quibusdam harum dolores. Nam, reprehenderit suscipit? Alias voluptas non quos voluptatibus aperiam rem error nihil dicta asperiores blanditiis. Lorem ipsum dolor, sit amet consectetur adipisicing elit. Vitae nobis porro rerum pariatur! Architecto ab adipisci exercitationem rem veniam cupiditate, animi dignissimos esse facilis aut reprehenderit hic voluptatem nesciunt error.".split(' ')
  const [scrollContent,setScrollContent] = useState([..."This page was created to practice React with useOutletContext and Navigate functions. More text more text more text more text more textddd."])
  const [scrolling, setScrolling] = useState([])
  const [currentPlace,setCurrentPlace] = useState(0)


  const loadText = () =>{
    if (currentPlace<=scrollContent.length) {
      setScrolling(oldScroll => [...oldScroll,scrollContent[currentPlace]])
      setCurrentPlace(currentPlace+1)
    } else {

      const tempScroll = scrollContent
      tempScroll.splice(0,0)
      console.log(tempScroll)
      setScrolling(oldScroll => [...oldScroll.splice(1,oldScroll.length-1),scrollContent[currentPlace]])
      // setCurrentPlace(currentPlace-1)
      // setCurrentPlace(currentPlace-2)
      // setCurrentPlace(currentPlace+1)
     }
  
  }
  
  
const getLorem = () => {
  
  const held = [];
  const randLength = Math.floor(Math.random()*10)+5;
  for (let x = 0;x<randLength;x++) {
    const rand = Math.floor(Math.random()*lorem.length);
    held.push(lorem[rand])
  }
  const tempScroll = scrollContent.join('')
  // console.log(tempScroll)
  const tempHold = held.join(' ')
  // console.log(held.join(' '))
  const tempText = (tempScroll + " " + tempHold).split('')
  // console.log(tempText)
  

  return tempText
}

  const updateText = () => {
    // let lor = getLorem();
    // lor = [...lor];
    // const combineIt = scrollContent & lor;
    // console.log(combineIt)
    // setScrollContent(oldScroll => [oldScroll,getLorem()])
    setScrollContent(getLorem())
    
  }

useEffect(() => {
// if(currentPlace>0){
//   setCurrentPlace(0)
//   loadText()
// }
loadText()
},scrollContent)

useEffect(() => {
loadText()
},scrolling)

  return (
<>
    <div>HomePage</div>

    <div className={'scroll'}>
      {scrolling}
    </div>
    <button onClick={() => {updateText()}}>Add More</button>
</>
  )
}
