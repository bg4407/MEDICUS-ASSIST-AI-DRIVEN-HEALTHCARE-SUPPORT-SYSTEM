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
            {/* Dialogflow Messenger */}
            <df-messenger
                location="us-central1"
                project-id="medicus-assist"
                agent-id="77a5a9f8-0f47-4c21-a001-636d18737bad"
                language-code="en"
                max-query-length="-1">
                <df-messenger-chat-bubble
                    chat-title="Medicus Assist">
                </df-messenger-chat-bubble>
            </df-messenger>
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
