import React from 'react';
import { Navigate } from 'react-router-dom';

const ProtectedRoute = ({ element }) => {
  const user = localStorage.getItem('token'); // Example: Fetch user token from localStorage

  // Redirect to login if no user is found
  return user ? element : <Navigate to="/login" />;
};

export default ProtectedRoute;