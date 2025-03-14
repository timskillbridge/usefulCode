// import { Component } from "react"

// npm install react-router-dom
// mkdir pageXOffset
// touch HomePage

// Page is basically a Component

// import React from 'react'

// export default function HomePage() {
//   return (
    
//   }

//   move up to assets src directory and create a router.jsx

//   import { createBrowserRouter } from "react-router"
//   import App from './App.jsx'
//   import HomePage from "./pages/HomePage.jsx"

//   const router = createBrowserRouter( {
//     {
//         //http://localhost:5173
//         path:'/'
//         //this is the component to render as 
//         element: <App />
//         //children which rep pages on the app
//         chidlren: [
//             {element:<HomePage />}
//         ]
//     }
//   })

//   import router into main.jsx (make sure to export it in router)
//   import { RouterProvider } from "react-router-dom"

//   change 'App" in main.jsx to 
//   <RouterProvider router={router}'

//   go to main App.jsx
//   import { outlet } from 'react-router-dom'
//   add <Outlet /> to return statement