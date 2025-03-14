

//Flip a card over and zoom in
//Relies on dynamic classa application on div




The css:

.flip-container {
    perspective: 1000px;
    width: 200px; /* Adjust the size as needed */
    height: 200px; /* Adjust the size as needed */
  }
  
  .flipper {
    position: relative;
    width: 100%;
    height: 100%;
    transform-style: preserve-3d;
    transition: transform 1s;
    transform: rotateY(-180deg);
  }
  
  .flip-container:active .flipper {
    transform: rotateY(0deg) scale(2);
    position: absolute;
    top:45%;
    left:45%;
  }



  Flash useEffect is applied by dynamically applying a class based on a useCase boolean value, updated by a button onClick

  <div className={`flip-container ${flash? 'flashing-div':''}` }>   //The dynamic application

  const [flash,setFlash] = useState(false)  //The useState

    // The button

    const handleSubmit = (e) => {
        e.preventDefault();
        setFormInput("")
        console.log(`testing button input ${formInput}`)
        setSingleMon(`${formInput}`)
        setFlash(true)
        setTimeout(() =>{
          setFlash(false)
        },500)



  .flashing-div{
  background-image: url('your-image-url.jpg');
  background-size: cover;
  background-position: center;
  opacity: 1;
  transition: opacity 0.5s;
  opacity:.8;
}

