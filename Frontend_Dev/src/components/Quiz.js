import React, { useState, useEffect, useContext } from 'react';
import Confetti from 'react-confetti'; // For confetti animation
import './style/Quiz.css'; // Import the CSS file
import { AuthContext } from './AuthContext';
import { useNavigate } from 'react-router-dom';
import {  fetchQuestions, submitQuiz } from './Api';

const Quiz = ({ category }) => {
    const { user } = useContext(AuthContext);
    const navigate = useNavigate();

    const [questions, setQuestions] = useState([]);
    const [answers, setAnswers] = useState({});
    const [score, setScore] = useState(null);

    useEffect(() => {
        if (!user) {
            navigate('/login'); // Redirect to login if user is not authenticated
            return;
        }

        const getQuestions = async () => {
            try {
                const data = await fetchQuestions(category);
                setQuestions(data);
            } catch (error) {
                console.error('Error fetching questions:', error);
            }
        };
        getQuestions();
    }, [user, category, navigate]);

    const handleAnswerChange = (questionIndex, answer) => {
        setAnswers({
            ...answers,
            [questionIndex]: answer,
        });
    };

    const handleSubmit = async (event) => {
        event.preventDefault(); // Prevent form from submitting traditionally
        try {
            const result = await submitQuiz(category, answers);
            setScore(result.score);
        } catch (error) {
            console.error('Error submitting quiz:', error);
        }
    };

    return (
        <div>
            <h1>Quiz: {category}</h1>
            {score !== null && <Confetti />}
            <form onSubmit={handleSubmit}>
                {questions.map((q, index) => (
                    <div key={index}>
                        <h3>{q.question}</h3>
                        {q.answers.map((answer) => (
                            <label key={answer}>
                                <input
                                    type="radio"
                                    name={`question_${index}`}
                                    value={answer}
                                    onChange={() => handleAnswerChange(index, answer)}
                                />
                                {answer}
                            </label>
                        ))}
                    </div>
                ))}
                <button type="submit">Submit Quiz</button>
            </form>
            {score !== null && <p>You scored: {score}</p>}
        </div>
    );
};

export default Quiz;