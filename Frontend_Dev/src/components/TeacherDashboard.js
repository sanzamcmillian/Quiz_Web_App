import React, { useState, useEffect } from 'react';
import { Line } from 'react-chartjs-2';
import Chart from 'chart.js/auto';
import './style/TeacherDashboard.css';

const TeacherDashboard = () => {
  const [studentResults, setStudentResults] = useState([]);

  useEffect(() => {
    // Fetch all student results
    const fetchStudentResults = async () => {
      try {
        const response = await fetch('/api/all-student-results'); // Adjust endpoint accordingly
        const data = await response.json();
        setStudentResults(data);
      } catch (error) {
        console.error('Error fetching student results:', error);
      }
    };

    fetchStudentResults();
  }, []);

  // Prepare data for the chart
  const chartData = {
    labels: studentResults.map(result => result.date),
    datasets: [
      {
        label: 'Student Scores',
        data: studentResults.map(result => result.score),
        fill: false,
        backgroundColor: 'rgba(75, 192, 192, 0.2)',
        borderColor: 'rgba(75, 192, 192, 1)',
        tension: 0.1
      }
    ]
  };

  return (
    <div className="teacher-dashboard-container">
      <h2>Teacher Dashboard</h2>
      <div className="chart-container">
        <Line data={chartData} />
      </div>
      <div className="results-list">
        <h3>All Student Results</h3>
        <ul>
          {studentResults.map((result, index) => (
            <li key={index}>
              <p>Student ID: {result.studentId}</p>
              <p>Date: {result.date}</p>
              <p>Score: {result.score}</p>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default TeacherDashboard;