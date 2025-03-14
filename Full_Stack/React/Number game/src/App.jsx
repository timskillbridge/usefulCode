import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const num = Math.floor(Math.random()*101)

  const handleSubmit = (evt) => {
      evt.preventDefault()
      let userGuess = document.getElementById('user-guess')
      let userMsg = document.getElementById('user-msg')
      if(userGuess.value > num) {
        userMsg.innerText = "too high"
        userGuess.value = ""
      }
      else if (userGuess.value < num) {
        userMsg.innerText = "too low"
        userGuess.value = ""
      } else {userMsg.innerText = "got it"}
  }

  return (
    <>
      <h1>Guess a number</h1>
      <div id="user-msg"></div>
      <form onSubmit={(event)=>handleSubmit(event)} >
        <input type="number" id="user-guess" max={100} min={1} name="intake"/>
        <input type="submit" value="submit"/>
      </form>
    </>
  )
}

export default App
