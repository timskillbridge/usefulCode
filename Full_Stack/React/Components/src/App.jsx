import { useState, useEffect} from 'react'
import './App.css'
import ListItem from './Components/ListItem'
import axios from 'axios'
import jsonTasks from './tasks.json'



function App() {

  const [tasks, setTasks] = useState(jsonTasks);
  

  useEffect(() => {
    console.log(tasks);
  },[tasks]);

  const setTasksCompleted = () => {
    // filter returns a copy of the og array
    setTasks(jsonTasks.filter((task) => task.completed));
  };

  const setTasksIncompleted = () => {
    setTasks(jsonTasks.filter((task) => !task.completed));
  };
  

  return (
    <>
    <h1>To Do List</h1>
    <button onClick={() => setTasks(jsonTasks)}>All Tasks</button>
      <button onClick={setTasksCompleted}>Completed Only</button>
      <button onClick={setTasksIncompleted}>Incomplete Only</button>

    <ul>
      {tasks.map((task) => (
        <ListItem key={task.id} propTask = {task} />
      ))}
    </ul>
    </>
  )
}

export default App
