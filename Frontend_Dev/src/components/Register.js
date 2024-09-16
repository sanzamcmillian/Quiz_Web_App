import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { register } from './Api'; // Import the register function from Api.js
import './style/Register.css'; // Import the CSS file

const Register = () => {
  const [name, setName] = useState('');
  const [surname, setSurname] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      setError('Passwords do not match');
      return;
    }

    try {
      const response = await register({ name, surname, email, password });
      if (response.status === 201) { // Assuming success status code is 201
        navigate('/login'); // Redirect to login page after successful registration
      } else {
        setError('Failed to register');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handleRegister();
  };

  return (
    <div className="register-container">
      <div className="register-form">
        <h2>Register</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="Name"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Surname"
            value={surname}
            onChange={(e) => setSurname(e.target.value)}
            required
          />
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
          <input
            type="password"
            placeholder="Confirm Password"
            value={confirmPassword}
            onChange={(e) => setConfirmPassword(e.target.value)}
            required
          />
          <button type="submit">Register</button>
          {error && <p className="error-message">{error}</p>}
        </form>
      </div>
    </div>
  );
};

export default Register;