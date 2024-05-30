import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import InitialPage from './components/InitialPage';
import Login from './components/Login';
import SignUp from './components/SignUp';
import ChatInterface from './components/ChatInterface';
import SidePanel from './components/SidePanel';
import './App.css';

function ChatPage() {
    
    const handleSelectExample = (example) => {
        console.log("Example selected:", example); 
    };

    return (
        <div className="chat-page">
            <SidePanel onSelectChat={(id) => console.log("Chat selected:", id)} />
            <ChatInterface onSelectExample={handleSelectExample} />
        </div>
    );
}

function App() {
    return (
        <Router>
            <Routes>
                <Route path="/" element={<InitialPage />} />
                <Route path="/login" element={<Login />} />
                <Route path="/signup" element={<SignUp />} />
                <Route path="/chat" element={<ChatPage />} />
            </Routes>
        </Router>
    );
}

export default App;
