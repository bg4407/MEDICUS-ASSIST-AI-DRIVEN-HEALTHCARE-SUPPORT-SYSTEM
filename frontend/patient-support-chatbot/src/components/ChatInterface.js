import React, { useState } from 'react';
import './ChatInterface.css';
import Dashboard from './Dashboard';

function ChatInterface() {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = (message = input) => {
        if (!message.trim()) return;

        const newMessages = [...messages, { type: 'user', text: message }];
        setMessages(newMessages);
        setInput('');
    };

    const handleExampleSelect = (example) => {
        sendMessage(example);
    };

    return (
        <div className="chat-interface">
            {messages.length === 0 && <Dashboard onSelectExample={handleExampleSelect} />}
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.type === 'user' ? 'user-message' : 'bot-message'}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input
                type="text"
                value={input}
                onChange={(e) => setInput(e.target.value)}
                onKeyPress={(e) => { if (e.key === 'Enter') sendMessage(); }}
                placeholder="Type your message..."
            />
            <button onClick={() => sendMessage()}>Send</button>
        </div>
    );
}

export default ChatInterface;
