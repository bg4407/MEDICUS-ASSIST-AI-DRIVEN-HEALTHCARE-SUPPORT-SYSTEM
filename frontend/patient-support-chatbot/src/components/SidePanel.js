import React from 'react';
import './SidePanel.css';
import { useNavigate } from 'react-router-dom';

function SidePanel() {
    const navigate = useNavigate();

    return (
        <div className="side-panel">
            <div className="panel-footer">
                <button onClick={() => navigate('/login')} className="logout-button">Log out</button>
            </div>
        </div>
    );
}

export default SidePanel;
