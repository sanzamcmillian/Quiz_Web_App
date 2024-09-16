// src/components/AuthContext.js
import React, { createContext, useState, useEffect } from 'react';

// Create the AuthContext
export const AuthContext = createContext();

// AuthProvider to wrap around the app and provide user state
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // State to store the authenticated user

  // Load user from localStorage on initial render
  useEffect(() => {
    const storedUser = localStorage.getItem('user');
    if (storedUser) {
      setUser(JSON.parse(storedUser));
    }
  }, []);

  const login = (userData) => {
    setUser(userData); // Set the user when they log in
    localStorage.setItem('user', JSON.stringify(userData)); // Save the user to localStorage
    localStorage.setItem('token', userData.token); // Assuming the token is part of userData
  };

  const logout = () => {
    setUser(null); // Clear the user when they log out
    localStorage.removeItem('user'); // Clear user from localStorage
    localStorage.removeItem('token'); // Clear token from localStorage
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};