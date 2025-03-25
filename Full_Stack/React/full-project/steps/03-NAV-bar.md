
Make components directory

create NavBar.jsx
-----------------------

import {Link} from 'react-router-dom'

const NavBar = () => {

    return (

        <ul style={{ display:'flex', justifyContent:'space-around'}}>
            <li>
            <Link to={'/'}>Home</Link>
            </li>
            <li>
            <Link to={'/about/'}>About</Link>
            </li>
            <li>
            <Link to={'/characters/'}>Characters</Link>
            </li>
        </ul>

    );
};

export default NavBar

in App.jsx:
    import { Outlet } from 'react-router'dom'
    import NavBar into App.jsx
    Add link to <NavBar /> in App.jsx
    Below <NavBar /> add <Outlet />