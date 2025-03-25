
Create pages directory with applicable pages .jsx files
    use rfc to do it quickly

Create router.jsx in src directory
------------------------------------

import { createBrowserRouter } from 'react-router-dom';
import App from './app';
import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage';
import CharactersPage from './pages/CharactersPage'

const router = createBrowserRouter([

    {
        path: '/',
        element: <App />,
        children: [
            {
                index: true,
                element: <HomePage />,
            },
            {
                path: '/characters/',
                element: <CharactersPage />,
            },
            {
                path: '/about/',
                element: <AboutPage />
            }

        ],
        
}
])

export default router