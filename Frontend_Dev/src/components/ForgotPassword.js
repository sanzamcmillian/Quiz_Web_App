import React, { useState } from 'react';
import { requestPasswordReset } from './Api'; // Import the requestPasswordReset function from Api.js
import Login from './Login';
import './style/ForgotPassword.css'; // Import the CSS file

const ForgotPassword = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [error, setError] = useState('');

  const handlePasswordResetRequest = async () => {
    try {
      const response = await requestPasswordReset(email);
      if (response.status === 200) {
        setMessage('Password reset link has been sent to your email.');
      } else {
        setError('Failed to send password reset link.');
      }
    } catch (err) {
      setError('An error occurred. Please try again.');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    handlePasswordResetRequest(); // Call handlePasswordResetRequest on form submit
  };

  return (
    <div className="forgot-password-container">
      <div className="forgot-password-form">
        <h2>Forgot Password</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <button type="submit">Send Reset Link</button>
          {message && <p className="success">{message}</p>}
          {error && <p className="error">{error}</p>}
        </form>
      </div>
    </div>
  );
};

export default ForgotPassword;