

npm create vite .
npm install
npm install axios
npm install react-router-dom

in main.jsx
import { Router } from 'react-router-dom';
    remove strict mode
render RouterProvider
--------------------
import React from 'react'
import { render } from 'preact'
import './index.css'
import { App } from './app.jsx'
import { RouterProvider } from 'react-router-dom';
import router from './router.jsx'

render(<RouterProvider router ={router} />, document.getElementById('app'))


OPTIONAL
npm install boostrap react-bootstrap
    place bootstrap css file in main.jsx:
    import 'bootstrap/dist/css/bootstrap.min.css';

npm install tailwindcss @tailwindcss/vite
remove strict mode from main.jsx
remove css from index.css and app.css


