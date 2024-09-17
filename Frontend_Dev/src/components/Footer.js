import React from 'react';
import './style/Footer.css';

const Footer = () => {
  return (
    <footer className="bg-dark text-white text-center py-3">
      <div className="container">
        <p>&copy; 2024 QuizApp. All Rights Reserved.</p>
        <p>
          <a href="/about" className="text-white me-2">About</a> | 
          <a href="/contact" className="text-white ms-2">Contact</a>
        </p>
      </div>
    </footer>
  );
};

export default Footer;
