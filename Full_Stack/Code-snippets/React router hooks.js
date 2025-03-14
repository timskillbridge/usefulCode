

// useContext allows you to share data with every aspect of an application without chaining props

//  Create context for the application in a new file called context.ts

{(`
1.  Kill strict mode
2. import all appropriate boostrap/tailwind
    main.jsx import boostrap
3. kill default css
4. import {RouterProvider} from 'react-router-dom';  in main .jsx
import router from './router.jsx'  ...once built
    ReactDOM.createRoot(document.getElementById
    ("root")).render(<RouterProvider router={} />);
5. create pages (HomePage, etc...).jsx
    each can be populated using rfc
6. create router in src/router.jsx
    import {createBrowserRouter } from 'react-router-dom'
    import App from "./App";
    import pages you made from their Pages directory

    export default const router = createBrowserRouter({
    [
        {
            path: '/',
            element: <App/>
            children: [
            
            {
            index:true,
            element: <HomePage />
            },
            
            {
            path: '/data',
            element: <DataPage/>
            },
            
            ],
        }
    ]    
    }
)

7. build nav bar component
    use boostrap or just an unordered list with Link in each nested list item : <Link to={'/'}>Home</Link>    .... etc
    import {Link} from 'react-router-dom';

8. put nav bar in App.jsx's return statement <NavBar/> followed by <Outlet/>

9. create function in page that needs to build pages dynamically, 
    request data with an api
    iterate through array of objects
    create content for each thing.
    will require a useState and useEffect

    const [allData,setAllData] = useState([])

    const getApiData = async () => {
        try{
        let {data} = await axios.get("API LINK");
        setAllData(data)
        } catch (err) {
         alert(err)}
        
        }

        useEffect(() => {
            getData();
            })

        return {
        <h1>Appropriate title</h1>
        <>
        <ul>
        {
        allData.map((datum)=>(
            <li> <Link to=`/data/${data.id}`>{datum.desiredData}</Link></li>   <----------the variable data.id is coming from the set function above
            ))
        }
        </>
        </ul>

        }

10. Build the page for the data similar to the prior page but built on-the-fly based on input
    go back to router and add a child

    {
        path: '/data/:dataID',         <---------Same file path but add :and an ID
        element: <ADatum/>
    },

                            DON'T FORGET TO IMPORT IT AT THE TOP OF ROUTER!

    back to the page you were building
    define a useParams() function

export default ADatum = () => {

    const [datum,setDatum] = useState(null)
    const {dataID} = useParams()   <--------from the router, the path of data:dataID created this variable and puts it in the url

    const getADatum = async () => {
        try{
        let {data} = await axios.get("API address")
        setDatum(data)
        } catch (err) {
         console.log(err)
         }
        }

    useEffect(() => {
        getADatum())
    },[])

    return {
    
<>
{
datum?
whatever you want here
<img src={...}/>

<h3>Title, name, whatever<h3/>
: loading
}
</>

    }
}

11. Go back to your data page to create the navigation hook
        Until now navigation was being done by a Link
          <li> <Link to=`/data/${data.id}`>{datum.desiredData}</Link></li>   <----------the variable data.id is coming from the set function above

    const nagivation = useNavigate();
    change the above to 
    <li key={index} onClick={() => navigate(`/data/${data.id}`}> Desired display </li>

    12. build the validate response function if desired
        within the dynamically created page for individual dataum still

        const validateResponse = async (dataID) => {
            let {data} = await axios.get("api call")
            data['response] = await axios.get("api call",{validateStatus: () => true,})
            if (data['response'] === 200) {
            navigattion(`/data/${dataID}`)
            } else {alert('something done fucked up')
             }
            }
12. Update the onClick to be validateResponse(data.id)

13. implement useContext, lives in App.jsx so it can hand it down to children
    built a useState for the data

    const [rememberMe,setRememberMe] = useState([]);  --------Try to use an set within an array to avoid duplicates
                                    useState(() => {
                                        const holdingSet = new Set
                                        return holdingSet
                                        })

    const addToRememberMe = ((val) => {
        setRememberMe(r,val}
        })

    const remoeveRememberMe = (val) => {
        setRememberMe(r.filter((item) => (item.id !== val.id)))
        }

14. add context to Outlet in App.jsx
<Outlet context={{addToRememberMe, removeRememberMe, rememberMe}} />

stopped at 1 hour 16 30


favorites:

create favorites page

const FavoritesPage = () => {
    
    return 
    <>
    whatever you want
    </>
    
    }

create OutletContext

in App.jsx

useState for favorites
const [favorites,setFavorites] = useState([])

const addToFavs = (char) => {
    if(favorites.filter((fav)=> fav.id == char.id) || favorites.length >3) {
    alert(no bueno)
    } else {
     setFavorites([...fav,char])}
    }

const removeFromFavs = (char) => {
    setFavorites(favorites.filter((fav) => fav.id !== char.id))
    }

const isFav = (char) => {
    if (favorites.filter((fav) => fav.id).length)}

const{isFav, addToFavs, removeFromFavs} = useOutletContext()
    return (
    <navBar />
    <Outlet context = use>
    
    )
`)}