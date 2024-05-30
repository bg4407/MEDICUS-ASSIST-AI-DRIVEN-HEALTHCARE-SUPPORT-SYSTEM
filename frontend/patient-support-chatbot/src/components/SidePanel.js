import React, { useState } from 'react';
import './SidePanel.css';
import { useNavigate } from 'react-router-dom';

function SidePanel({ onSelectChat }) {
    const [chats, setChats] = useState([]);
    const navigate = useNavigate();

    const handleNewChat = () => {
        const newChatId = chats.length + 1;
        const newChat = { id: newChatId, title: `Chat ${newChatId}` };
        setChats([...chats, newChat]);
        onSelectChat(newChatId);
    };

    return (
        <div className="side-panel">
            <button onClick={handleNewChat} className="new-chat-button">+ New Chat</button>
            {chats.map(chat => (
                <div key={chat.id} className="chat-item" onClick={() => onSelectChat(chat.id)}>
                    {chat.title}
                </div>
            ))}
            <div className="logout-button" onClick={() => {navigate('/login');}}>Log out</div>
        </div>
    );
}

export default SidePanel;
