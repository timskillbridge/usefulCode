
document.getElementById('header-text').classList.toggle('main')

submitName = () =>{
    let userInput = document.getElementById('user-input');
    let output = document.getElementById('output');
    output.innerText = userInput.value;
    userInput.value = "";
}

createCard = () => {
    let container = document.querySelector("#container")
    let newCard = document.createElement('div')
    newCard.classList.add('card')
    newCard.addEventListener('mouseover',(evt) => {
        let randCol = `rgb(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)},
        ${Math.floor(Math.random() * 256)})`;
        evt.target.style.backgroundColor = randCol
    })
    imgNum = randImg()
    
    img = document.createElement('img')

    img.src =  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + imgNum +".png"
    
    newCard.appendChild(img)
    
    
    container.appendChild(newCard)
}

showImg = () => {
    let container = document.querySelector('#img-container')
    let img = document.createElement('img')
    imgNum = randImg()
    img.src =  "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + imgNum +".png"
    container.appendChild(img)
}

handleSubmit = (evt) => {
    evt.preventDefault()
    let formData = new FormData(evt.target)
    let formObj = Object.fromEntries(formData)
    // turns submitted data into key value pairs
    let ul = document.querySelector("#put-here")
    let li = document.createElement('li')
    let appendText = ""
    for (let key in formObj) {
        console.log("asdf")
        appendText = `${key} : ${formObj[key]}`
    }
    // for (let key in formObj) {
    // }    
    li.innerText = appendText
    ul.appendChild(li)
    
}

randImg = () => {
    return Math.floor(Math.random() *150)
}