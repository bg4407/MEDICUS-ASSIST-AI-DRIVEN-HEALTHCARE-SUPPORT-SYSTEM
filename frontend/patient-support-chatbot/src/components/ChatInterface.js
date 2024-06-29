import React, { useState } from 'react';
import axios from 'axios';
import './ChatInterface.css';
import Dashboard from './Dashboard';

function ChatInterface({ onSelectExample }) {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async (message = input) => {
        if (!message.trim()) return;

        const newMessages = [...messages, { type: 'user', text: message }];
        setMessages(newMessages);
        setInput('');

        try {
            const response = await axios.post('http://localhost:8080/chat', { message });
            const botMessage = { type: 'bot', text: response.data.response };
            setMessages([...newMessages, botMessage]);
        } catch (error) {
            console.error('Error communicating with the bot', error);
        }
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
