
const ListItem = ({prop}) => {
    return (
        <ul>
        <li>{`title: ${prop.title} Completed: ${prop.completed ? 'yes':'no'}`}</li>
        </ul>
    );
};

export default ListItem