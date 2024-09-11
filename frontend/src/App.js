// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import Feedback from './components/Feedback';
import Login from './components/Login';
import Register from './components/Register';
import SignUp from './components/SignUp';
import Quiz from './components/Quiz';
import Footer from './components/Footer';
import Welcome from './components/Welcome';
import StudentDashboard from './components/StudentDashoard';
import TeacherDashboard from './components/TeacherDashboard';
import ProtectedRoute from './components/ProtectedRoute';

import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap.bundle.min.js';

function App() {
  return (
      <Router>
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
          <Route path="/quiz" element={<Quiz />} />
          <Route path="/feedback" element={<Feedback />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
          <Route path="/register" element={<Register />} />
          <Route path="/welcome" element={<Welcome />} />
          
          {/* Protected Routes */}
          <Route path="/dashboard" element={<ProtectedRoute element={<StudentDashboard />} />} />
          <Route path="/teacher-dashboard" element={<ProtectedRoute element={<TeacherDashboard />} />} />
        </Routes>
        <Footer />
      </Router>
  );
}

export default App;