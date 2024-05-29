import React from 'react';
import { useNavigate } from 'react-router-dom';
import './InitialPage.css';

function InitialPage() {
    const navigate = useNavigate();

    return (
        <div className="initial-page">
            <div className="left-side">
                <div className="brand-title">Medicus Assist</div>
                <div className="quote">"<span className="bold">Schedule an appointment</span> for me with a dermatologist at 3 PM."</div>
            </div>
            <div className="right-side">
                <div className="get-started">Get started</div>
                <div style={{ display: 'flex', width: '100%' }}>
                    <button onClick={() => navigate('/login')} style={{ marginRight: '5px', flex: '1' }}>Log in</button>
                    <button onClick={() => navigate('/signup')} style={{ marginLeft: '5px', flex: '1' }}>Sign Up</button>
                </div>
            </div>
        </div>
    );
}

export default InitialPage;
