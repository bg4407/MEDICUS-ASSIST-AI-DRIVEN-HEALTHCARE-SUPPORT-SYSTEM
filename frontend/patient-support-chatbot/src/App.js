import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InitialPage from './components/InitialPage';
import Login from './components/Login';
import SignUp from './components/SignUp';
import ChatInterface from './components/Chat';

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<InitialPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />
                <Route path="/chat" element={<ChatInterface />} />
            </Routes>
        </Router>
    );
}

export default App;
