import React, { useState } from 'react';
import './ChatInterface.css';
import Dashboard from './Dashboard';

function ChatInterface({ onSelectExample }) {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (!input) return;

        const newMessages = [...messages, { type: 'user', text: input }];
        setMessages(newMessages);

        setInput('');
    };

    return (
        <div className="chat-interface">
            {/* Conditionally display Dashboard */}
            {messages.length === 0 && <Dashboard onSelectExample={onSelectExample} />}
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.type === 'user' ? 'user-message' : 'bot-message'}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input type="text" value={input} onChange={(e) => setInput(e.target.value)} placeholder="Type your message..." />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
}

export default ChatInterface;
