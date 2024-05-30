import React, { useState } from 'react';
import './SidePanel.css';

function SidePanel({ onSelectChat }) {
    const [chats, setChats] = useState([]); // State to handle dynamic chats

    const handleNewChat = () => {
        const newChatId = chats.length + 1; // Generate new chat ID
        const newChat = { id: newChatId, title: `Chat ${newChatId}` };
        setChats([...chats, newChat]); // Add new chat
        onSelectChat(newChatId); // Select new chat
    };

    return (
        <div className="side-panel">
            <button onClick={handleNewChat} className="new-chat-button">+ New Chat</button>
            {chats.map(chat => (
                <div key={chat.id} className="chat-item" onClick={() => onSelectChat(chat.id)}>
                    {chat.title}
                </div>
            ))}
            <div className="logout-button" onClick={() => {/* Add logout logic */}}>Log out</div>
        </div>
    );
}

export default SidePanel;
