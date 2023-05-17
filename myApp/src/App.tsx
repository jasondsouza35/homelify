import { useState } from 'react'
import './App.css'

function App() {

  const [formData, setFormData] = useState({
    address: '',
    size: ''
  });

  return (
    <>
      <p>Enter details:</p>

      <form action="" method="post">
        <label htmlFor="address">Address:</label> <br />
        <input type="text" id="address" name="address" /> <br />
        <br />

        <label htmlFor="size">Size (in sqft):</label> <br />
        <input type="text" id="size" name="size" /> <br />
        <br />

        <button type="submit" value="Submit">Submit</button>
      </form>
    </>
  )
}

export default App
