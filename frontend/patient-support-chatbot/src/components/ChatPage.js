import React, { useState } from 'react';
import SidePanel from './SidePanel';
import ChatInterface from './ChatInterface';
import { useUser } from '../UserContext'; // Correct path to UserContext
import '../App.css';

function ChatPage() {
    const [selectedChatId, setSelectedChatId] = useState(null);
    const { user } = useUser();

    if (!user) {
        return <div>Loading...</div>; // Or redirect to login
    }

    return (
        <div className="chat-page">
            <SidePanel onSelectChat={setSelectedChatId} userId={user.id} />
            <ChatInterface userId={user.id} selectedChatId={selectedChatId} setSelectedChatId={setSelectedChatId} />
        </div>
    );
}

export default ChatPage;
