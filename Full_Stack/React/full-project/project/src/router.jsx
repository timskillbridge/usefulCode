
import { createBrowserRouter} from 'react-router-dom';
import App from './app';
import HomePage from './pages/HomePage'
import AboutPage from './pages/AboutPage';
import CharactersPage from './pages/CharactersPage'
import Favorites from './pages/Favorites'
import ACharacter from './pages/ACharacter';


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
            },
            {
                path: '/characters/:characterID/',
                element: <ACharacter />
            },
            {
                path: '/favorites/',
                element: <Favorites/>
            }

        ],
        
}
])

export default router