// src/components/Welcome.js
import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import './style/Welcome.css';

const Welcome = () => {
  const { user } = useContext(AuthContext);
  const navigate = useNavigate();

  const startQuiz = () => {
    navigate('/quiz');
  };

  return (
    <div className="welcome-container">
      <h1>Welcome, {user ? user.email : 'User'}!</h1>
      <p>Congratulations on successfully logging in. You're now ready to start your quiz journey!</p>
      <button className="btn btn-primary" onClick={startQuiz}>Start Quiz</button>
    </div>
  );
};

export default Welcome;