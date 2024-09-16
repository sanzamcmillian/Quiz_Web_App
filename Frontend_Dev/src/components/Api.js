import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/';  // Backend server URL

// Function to register new users
export function register(userData) {
    return axios.post(`${API_URL}api/register/`, userData);  // Updated path
}

// Function to login users
export function login(userData) {
    return axios.post(`${API_URL}api/login/`, userData);  // Updated path
}

// Function to request a password reset
export function requestPasswordReset(email) {
    return axios.post(`${API_URL}auth/password-reset/`, { email });
}

// Function to logout users
export async function logout() {
    const token = localStorage.getItem('token');
    if (token) {
        try {
            await axios.post(`${API_URL}api/logout/`, {}, {  // Updated path
                headers: {
                    Authorization: `Token ${token}`
                }
            });
        } catch (error) {
            console.error('Logout error:', error);
        }
        localStorage.removeItem('token');
    }
}

// Function to fetch quizzes
export async function fetchQuestions(quizId) {
    const token = localStorage.getItem('token');
    if (!token) {
        throw new Error('No authentication token found');
    }
    try {
        const response = await axios.get(`${API_URL}quizzes/${quizId}/questions/`, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
        return response.data;
    } catch (error) {
        console.error('Error fetching questions:', error);
        throw error; // Optionally rethrow to handle in the component
    }
}

// Function to submit quiz answers
export async function submitQuiz(quizId, userData) {
    const token = localStorage.getItem('token');
    if (!token) {
        throw new Error('No authentication token found');
    }
    try {
        return await axios.post(`${API_URL}quizzes/${quizId}/submit/`, userData, {
            headers: {
                Authorization: `Token ${token}`
            }
        });
    } catch (error) {
        console.error('Error submitting quiz:', error);
        throw error; // Optionally rethrow to handle in the component
    }
}