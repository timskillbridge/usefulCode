

const getDog = async() => {                     //async required
    let url = 'https://random.dog/woof.json'    //The API being called
    let response = await fetch(url);            //the response, note the await
    let data = await response.json()            //turn the response into something we can iterate
    let passUrl = data['url']                   //grabe the data you need
    generateCard(passUrl)                       //pass to external function to use the data. 
}

const getDogs = async() => {
    let url = 'https://random.dog/woof.json'
    let {data} = await axios.get(url)
    content = data['key you care about']
    SVGComponentTransferFunctionElement(conetent)
}

//Use the API to generate content
generateCard = (url) => {
    let container = document.querySelector('#image-container')
    let newCard = document.createElement('div')
    newCard.classList.add('dogcard')
    let cardImage = document.createElement('img')
    cardImage.src = url
    cardImage.classList.add('dogImg')
    newCard.appendChild(cardImage)
    container.appendChild(newCard)
}
