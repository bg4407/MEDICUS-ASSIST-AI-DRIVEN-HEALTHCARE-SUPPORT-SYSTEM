import React, { useState } from 'react';
import './Login.css';
import axios from 'axios';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (event) => {
        event.preventDefault();
        try {
            const response = await axios.post('http://localhost:5000/login', { username, password });
            console.log('Logged in!', response.data);
        } catch (error) {
            console.error('Failed to login', error.response.data);
        }
    };

    return (
        <div className="login-container">
            <div className="login-form">
                <h1>Welcome Back</h1>
                <form onSubmit={handleSubmit}>
                    <input type="text" value={username} onChange={(e) => setUsername(e.target.value)} placeholder="Username" required />
                    <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} placeholder="Password" required />
                    <button type="submit">Login</button>
                    <p className="signup-link">Don't have an account? <a href="/signup">Sign up</a></p>
                </form>
            </div>
        </div>
    );
}

export default Login;
