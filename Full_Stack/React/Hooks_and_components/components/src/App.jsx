import { useEffect, useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import jsonTasks from './tasks.json'
import ListItem from './Components/ListItem.jsx'
import './App.css'
import axios from 'axios'

function App() {
const [tasks, setTasks] = useState(jsonTasks)

useEffect(() => {
  console.log(tasks);
}, [tasks]);

const completedTasks = () => {
  setTasks(jsonTasks.filter((task) => task.completed))
}

const incompleteTasks = () => {
  setTasks(jsonTasks.filter((task) => task.incompleteTasks))
}

const hideTask =  (id) => {
  setTasks(tasks.filter((task) => task.id != id));
}


  return (
    <>
      <h1>To Do List</h1>
      <button onClick={() => setTasks(jsonTasks)}>All Tasks</button>
      <button onClick={() => completedTasks}>Completed Tasks</button>
      <button onClick={() => incompleteTasks}>Incomplete Tasks</button>
      <ul>
        {tasks.map((task) =>(
          <ListItem prop = {task} />
          
        ))}
      </ul>
    </>
  )
}

export default App
