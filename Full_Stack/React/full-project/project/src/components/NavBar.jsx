
import {Link, useNavigate} from 'react-router-dom'


const NavBar = () => {
const navigate = useNavigate()
    return (

        <ul style={{ display:'flex', justifyContent:'space-around'}}>
            <li onClick={() => navigate('/')}> 
            Home
            </li>
            <li onClick={() => navigate('/about/')}>
            About
            </li>
            <li onClick={() => navigate('/characters/')}>
            Characters
            </li>
            <li onClick={() => navigate('/favorites/')}>
            Favorites
            </li>
        </ul>

    );
};

export default NavBar