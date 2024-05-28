import React, { useEffect } from 'react';
import axios from 'axios';

function App() {
  useEffect(() => {
    axios.get('http://localhost:5000/')
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <p>Edit <code>src/App.js</code> and save to reload.</p>
      </header>
    </div>
  );
}

export default App;
