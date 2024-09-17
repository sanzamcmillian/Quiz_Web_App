// src/components/Welcome.js
import React, { useContext, useEffect } from 'react';
import { AuthContext } from './AuthContext';
import { useNavigate } from 'react-router-dom';
import './style/Welcome.css';

const Welcome = () => {
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  useEffect(() => {
    if (!user) {
      // Redirect to login if user is not authenticated
      navigate('/login');
    }
  }, [user, navigate]);

  const startQuiz = () => {
    if (user) {
    navigate('/quiz');
  }
};

  return (
    <div className="welcome-container">
      <h1>Welcome, {user ? user.email : 'User'}!</h1>
      <p>Congratulations on successfully logging in. You're now ready to start your quiz journey!</p>
      <button 
      className="btn btn-primary" 
      onClick={startQuiz}
      disabled={!user} // Disable the button if the user is not logged in
      >
      Start Quiz
      </button>
    </div>
  );
};

export default Welcome;