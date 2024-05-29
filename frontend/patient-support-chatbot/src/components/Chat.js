import React, { useState } from 'react';
import axios from 'axios';

function ChatInterface() {
    const [input, setInput] = useState('');
    const [messages, setMessages] = useState([]);

    const sendMessage = async () => {
        if (!input) return;
        
        const newMessages = [...messages, { type: 'user', text: input }];
        setMessages(newMessages);

        const botResponse = await axios.post('API_URL', { prompt: input });

        setMessages([...newMessages, { type: 'bot', text: botResponse.data.response }]);
        setInput('');
    };

    return (
        <div>
            <div className="messages">
                {messages.map((msg, index) => (
                    <div key={index} className={msg.type === 'user' ? 'user-message' : 'bot-message'}>
                        {msg.text}
                    </div>
                ))}
            </div>
            <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
            <button onClick={sendMessage}>Send</button>
        </div>
    );
}

export default ChatInterface;
