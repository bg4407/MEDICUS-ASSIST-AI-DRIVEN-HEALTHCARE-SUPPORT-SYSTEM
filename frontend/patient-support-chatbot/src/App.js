// App.js
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InitialPage from './components/InitialPage';
import Login from './components/Login';
import SignUp from './components/SignUp';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<InitialPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />
            </Routes>
        </Router>
    );
}

export default App;
