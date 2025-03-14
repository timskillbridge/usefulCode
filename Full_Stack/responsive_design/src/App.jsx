import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <h1>Responsive Design</h1>
      <div className="boxed" id="box1">
        <div id="box2"></div>
      </div>
      <div>
        <p className="p">
        <img id="pokeImg" src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png" alt="Ditto" />
          Lorem ipsum dolor sit amet consectetur, adipisicing elit. Odit ea cumque rem obcaecati, dolore esse dignissimos a, sunt, error doloremque voluptates voluptatem dolores temporibus illo voluptatibus culpa eius necessitatibus et? Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores laudantium, ducimus beatae expedita ea minima assumenda accusamus incidunt eius.
          Labore nam provident suscipit perferendis maxime aliquam dolorum alias totam temporibus!
      </p>
          

      </div>
      <div id="container">
        <div className="box">1</div>
        <div className="box">2</div>
        <div className="box">3</div>
        <div className="box">4</div>
        <div className="box" id="theBox">5</div>
        <div className="box">6</div>
        <div className="box">7</div>
        <div className="box">8</div>
        <div className="box">9</div>
        <div className="box">10</div>
          <div className="box">11</div>
          <div className="box">12</div>
          <div className="box">13</div>
          <div className="box">14</div>
          <div className="box">15</div>
          <div className="box">16</div>
          <div className="box">17</div>
          <div className="box">18</div>
          <div className="box">19</div>
          <div className="box">20</div>
          <div className="box">21</div>
          <div className="box">22</div>
          <div className="box">23</div>
          <div className="box">24</div>
          <div className="box">25</div>
          <div className="box">26</div>
          <div className="box">27</div>
          <div className="box">28</div>
          <div className="box">29</div>
          <div className="box">30</div>
        </div>
      
        <div id="outer">
          <div className="nested" id="middle">
            <div className="nested" id="inner"></div>
          </div>
        </div>
        <div>

      </div>
      Inline blocks
      <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"/>
      <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"/>
      <img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"/>
    </>
  )
}

export default App
//html shorthand for item with children
// div#clasName>div.box*9
/*   h1, h2, h3, div, etc..
Block tags are blocks occupying the entire width of their container in a column
      respects height and width but cuts elements from being displayed  next to it

INLINE-BLOCK TAGS: changes dispaly from column to row, shrinks box to size of content only

POSITIONING:
fixed: forces the element in the position given, allows overlapping elements
  top, bottom, left, right options
relative: moves from assigned postion the increment specified
  top, bottom, left, right
absolute: similar to fixed but with the ability to move like relative; allows overlapping elements
          renders from the top left of the container if container is relative positioned
*/