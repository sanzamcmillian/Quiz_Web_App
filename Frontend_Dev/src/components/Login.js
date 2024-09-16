import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ForgotPassword from './ForgotPassword';
import { login } from './Api'; // Import the login function from Api.js
import './style/Login.css'; // Import the CSS file

const Login = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate(); // Hook for navigation

  const handleLogin = async () => {
    try {
      const response = await login({ email, password });
      
      // Assuming the response data contains the token
      const { token } = response.data;
      if (token) {
        // Save user token in localStorage
        localStorage.setItem('token', token);
        navigate('/dashboard'); // Navigate to the dashboard on successful login
      } else {
        setError('Failed to log in');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleLogin(); // Call handleLogin on form submit
  };

  return (
    <div className="login-container">
      <div className="login-form">
        <h2>Login</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit">Login</button>
          {error && <p>{error}</p>}
        </form>
        <p>
         Forgot your password? <a href="/forgot-password">Reset it here</a>
        </p>
        <p>
        Don't have an account? <a href="/register">Register here</a>
        </p>
      </div>
    </div>
  );
};

export default Login;