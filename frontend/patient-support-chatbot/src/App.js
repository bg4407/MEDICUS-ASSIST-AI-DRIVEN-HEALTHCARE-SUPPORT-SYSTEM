import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Login from './components/Login';

function App() {
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios.get('http://localhost:5000/')
      .then(response => {
        console.log(response.data);
      })
      .catch(error => {
        console.error('There was an error!', error);
      });
  }, []);

  const handleLogin = (username) => {
    console.log(`Welcome ${username}!`);
    setUser(username);
  };

  return (
    <div className="App">
      <header className="App-header">
        {user ? <p>Welcome {user}!</p> : <Login onLogin={handleLogin} />}
      </header>
    </div>
  );
}

export default App;
