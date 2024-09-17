// src/components/StudentDashboard.js
import React, { useState, useEffect, useContext } from 'react';
import { Line } from 'react-chartjs-2';
import { AuthContext } from './AuthContext';
import './style/StudentDashboard.css';

const mockData = [
  {
    "date": "2024-09-10",
    "score": 7
  },
  {
    "date": "2024-09-08",
    "score": 5
  },
  {
    "date": "2024-09-05",
    "score": 8
  }
];

const StudentDashboard = () => {
  const { user } = useContext(AuthContext); 
  const [quizResults, setQuizResults] = useState([]);

  useEffect(() => {
    // Simulate fetching data from API
    const fetchQuizResults = () => {
      setQuizResults(mockData);
    };

    fetchQuizResults();
  }, []);

  // Prepare data for the chart
  const chartData = {
    labels: quizResults.map(result => result.date),
    datasets: [
      {
        label: 'Quiz Scores',
        data: quizResults.map(result => result.score),
        fill: false,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.1
      }
    ]
  };

  return (
    <div className="dashboard-container">
      <h2>Student Dashboard</h2>
      <div className="chart-container">
        <Line data={chartData} />
      </div>
      <div className="results-list">
        <h3>Recent Quiz Results</h3>
        <ul>
          {quizResults.map((result, index) => (
            <li key={index}>
              <p>Date: {result.date}</p>
              <p>Score: {result.score}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default StudentDashboard;