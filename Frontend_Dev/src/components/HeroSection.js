import React from 'react';
import './style/HeroSection';

const HeroSection = () => {
  return (
    <div className="hero-section">
      <div className="container">
        <h1 className="display-4">Welcome to QuizApp!</h1>
        <p className="lead">Challenge yourself with the best quizzes.</p>
        <a href="/quiz" className="btn btn-primary btn-lg">Take a Quiz</a>
      </div>
    </div>
  );
};

export default HeroSection;
