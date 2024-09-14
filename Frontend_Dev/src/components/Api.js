import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/';  // Backend server URL

// Function to register new users
export function register(userData) {
    return axios.post(`${API_URL}auth/registration/`, userData);
}

// Function to login users
export function login(userData) {
    return axios.post(`${API_URL}auth/login/`, userData);
}

// Function to fetch quizzes
export function fetchQuestions(quizId) {
    return axios.get(`${API_URL}quizzes/${quizId}/questions/`, {
        headers: {
            Authorization: `Token ${localStorage.getItem('token')}`
        }
    });
}

// Function to Submit
export function submitQuiz(quizId, userData) {
    return axios.post(`${API_URL}quizzes/${quizId}/submit/`, userData, {
        headers: {
            Authorization: `Token ${localStorage.getItem('token')}`
        }
    });
}
