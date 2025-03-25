import React from 'react'
import { render } from 'preact'
import './index.css'
import { App } from './app.jsx'
import { RouterProvider } from 'react-router-dom';
import router from './router.jsx'

render(<RouterProvider router ={router} />, document.getElementById('app'))

