import React, { useState, useEffect } from 'react'

import Form from './Components/Form';
import Playlist from './Components/Playlist';



function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("http://localhost:5000/").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log("Failed expo")
        console.log(data)
      }
    )
  }, [])
    
  return (

  <div className='main-page'>
    <h1> SoundSavvy</h1>
    <Form />
    <Playlist />
  </div>
  )
}

export default App
