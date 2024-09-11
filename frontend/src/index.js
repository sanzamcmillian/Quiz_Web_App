// src/index.js (for React 18)
import React from 'react';
import { createRoot } from 'react-dom/client';
import './index.css';
import App from './App';
import { AuthProvider } from './components/AuthContext'; // Assuming you have an AuthProvider

const container = document.getElementById('root');
const root = createRoot(container); // React 18 syntax

root.render(
  <React.StrictMode>
    <AuthProvider>
      <App />
    </AuthProvider>
  </React.StrictMode>
);