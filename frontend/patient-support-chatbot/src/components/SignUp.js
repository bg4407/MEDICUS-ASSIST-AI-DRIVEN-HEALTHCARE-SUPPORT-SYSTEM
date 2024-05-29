import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './SignUp.css';

function SignUp() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/register', { username, password });
            console.log('Registered!', response.data);
            navigate('/login');
        } catch (error) {
            console.error('Failed to register', error.response.data);
        }
    };

    return (
        <div className="signup-container">
    <div className="signup-form">
        <h1>Create Your Account</h1>
        <form onSubmit={handleSubmit}>
            <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
            <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
            <button type="submit">Continue</button>
        </form>
        <p className="login-link">Already a member? <a href="/login">Log in</a></p>
    </div>
</div>

    );
}

export default SignUp;