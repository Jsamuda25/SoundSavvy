import React,{ useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState({});

  useEffect(() => {
    fetch("http://localhost:5000/")
    .then(
      response => response.json())
    .then(json => {
      setData(json)
      console.log(data)
    })
  }, {})
    
  return (
    <h1>
      {data.message}
    </h1>
  )
}

export default App
