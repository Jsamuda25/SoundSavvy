import React,{ useState, useEffect } from 'react'

function App() {
  const [data, setData] = useState([{}]);

  useEffect(() => {
    fetch("/").then(
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
    <h1>

    </h1>
  )
}

export default App