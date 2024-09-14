// src/components/AuthContext.js
import React, { createContext, useState } from 'react';

// Create the AuthContext
export const AuthContext = createContext();

// AuthProvider to wrap around the app and provide user state
export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null); // State to store the authenticated user

  const login = (userData) => {
    setUser(userData); // Set the user when they log in
  };

  const logout = () => {
    setUser(null); // Clear the user when they log out
  };

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};