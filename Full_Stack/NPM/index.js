
import tasks from "./tasks.json" with {type:"json"};
import axios from "axios";
console.log(tasks)

tasks.map((tasks)=> console.log(tasks.title))
// or
// let tasksTitles = tasks.map((task)=>task.title)
// or
// map
let tasksTitles = tasks.map((tasks) => {
    let title = tasks.title.toUpperCase()
    return title
})
//                     difference between map and filter.  Map returns result for everything in the array, filter will only return items meeting condition; filter resizes but map returns undefined
//filter
// let completedTask = tasks.filter((task) => {
//     if (task.completed) {
//         console.log(task.title,task.completed)
//         return task
//     }
// })
let completedTasks = tasks.filter((tx) => tx.completed); //evalutates to true so it is returned
// filter incomplete the same way
let incompleteTasks = tasks.filter((x) => !x.completed); //x or tasks, just variable names

// get pokemon using fetch and axios
const getDitto = async() => {
    let requestURL = "https://pokeapi.co/api/v2/pokemon/ditto"
    let response = await fetch(requestURL)
    console.log(request)
}

const getDitto2 = async () => {
    let requestedURL = "https://pokeapi.co/api/v2/pokemon/ditto"
    let {data} = await axios.get(requestedURL);
    console.log(data)
}



//can enclose all within try{} catch{} blocks