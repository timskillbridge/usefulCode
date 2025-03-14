
import {useState} from 'react'

const ListItem = ({ propTask}) => {
    const [show,setShow] = useState(true);
    const [downArrow, setDownArrow] = useState('I');
    const changeArrow = () => {
        if (downArrow == "I"){
            setDownArrow("-");
        } else {
            setDownArrow("I")
        }
    }
    return (
        <li>
            
            Title: {propTask.title}

            <p><button onClick={() => [setShow(!show), changeArrow()]}>{downArrow}</button></p>
            {show ? (
                
                <ul>
                    
                    <li>Completed: {propTask.completed ? 'yes' : 'no'}</li>
                    <li>ID: {propTask.id}</li>
                </ul>
            ) : null}
            
        </li>
    );
};

export default ListItem