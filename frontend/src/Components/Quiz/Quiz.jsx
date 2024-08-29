import React, { useState, useEffect } from 'react';
import './Quiz.css';
import Confetti from 'react-confetti'; // Import the confetti package

const Quiz = () => {
    const [timeLeft, setTimeLeft] = useState(20); // 20 seconds timer
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [score, setScore] = useState(0);
    const [showResults, setShowResults] = useState(false);
    const [quizStarted, setQuizStarted] = useState(false); // Track whether the quiz has started

    const questions = [
        {
            question: "What currency does South Africa use?",
            answers: ["Dollar", "Pound", "Euro", "Rand"],
            correctAnswer: "Rand",
        },
        {
            question: "Which planet is known as the Red Planet?",
            answers: ["Earth", "Mars", "Jupiter", "Saturn"],
            correctAnswer: "Mars",
        },
        {
            question: "What is the capital city of Japan?",
            answers: ["Beijing", "Seoul", "Tokyo", "Bangkok"],
            correctAnswer: "Tokyo",
        },
        {
            question: "Which element has the chemical symbol 'O'?",
            answers: ["Gold", "Oxygen", "Hydrogen", "Iron"],
            correctAnswer: "Oxygen",
        },
        {
            question: "What is the largest mammal in the world?",
            answers: ["Elephant", "Blue Whale", "Giraffe", "Great White Shark"],
            correctAnswer: "Blue Whale",
        },
        {
            question: "What is the square root of 64?",
            answers: ["6", "7", "8", "9"],
            correctAnswer: "8",
        },
        {
            question: "In which year did World War II end?",
            answers: ["1945", "1940", "1939", "1942"],
            correctAnswer: "1945",
        },
        {
            question: "Which language is primarily spoken in Brazil?",
            answers: ["Spanish", "French", "Portuguese", "English"],
            correctAnswer: "Portuguese",
        },
        {
            question: "Which ocean is the largest?",
            answers: ["Atlantic", "Indian", "Pacific", "Arctic"],
            correctAnswer: "Pacific",
        },
        {
            question: "Which country is known as the Land of the Rising Sun?",
            answers: ["China", "South Korea", "Japan", "Thailand"],
            correctAnswer: "Japan",
        },
    ];

    useEffect(() => {
        if (quizStarted && timeLeft > 0) {
            const timer = setTimeout(() => setTimeLeft(timeLeft - 1), 1000);
            return () => clearTimeout(timer); // Cleanup the timer
        } else if (timeLeft === 0) {
            handleNextQuestion(); // Move to the next question when the time is up
        }
    }, [timeLeft, quizStarted]);

    const handleAnswerClick = (answer) => {
        if (answer === questions[currentQuestionIndex].correctAnswer) {
            setScore(score + 1);
        }
        handleNextQuestion();
    };

    const handleNextQuestion = () => {
        if (currentQuestionIndex < questions.length - 1) {
            setCurrentQuestionIndex(currentQuestionIndex + 1);
            setTimeLeft(20); // Reset the timer for the next question
        } else {
            setShowResults(true);
        }
    };

    const handleStartQuiz = () => {
        setQuizStarted(true);
    };

    const handlePlayAgain = () => {
        setQuizStarted(false);
        setShowResults(false);
        setCurrentQuestionIndex(0);
        setScore(0);
        setTimeLeft(20);
    };

    if (!quizStarted) {
        return (
            <div className='container'>
                <h1>Welcome to the Quiz App</h1>
                <button onClick={handleStartQuiz}>Start Quiz</button>
            </div>
        );
    }

    if (showResults) {
        return (
            <div className='container'>
                {score >= 5 ? (
                    <>
                        <Confetti /> {/* Display confetti if the score is 5 or above */}
                        <h1>Congratulations!</h1>
                        <p>Your score is: {score} / {questions.length}</p>
                    </>
                ) : (
                    <div style={{ color: 'red' }}>
                        <h1>Failed</h1>
                        <p>Your score is: {score} / {questions.length}</p>
                    </div>
                )}
                <button onClick={handlePlayAgain}>Play Again</button>
            </div>
        );
    }

    return (
        <div className='container'>
            <h1>Quiz App</h1>
            <hr />
            <h2>{questions[currentQuestionIndex].question}</h2>
            <ul>
                {questions[currentQuestionIndex].answers.map((answer, index) => (
                    <li key={index} onClick={() => handleAnswerClick(answer)}>{answer}</li>
                ))}
            </ul>
            <button onClick={handleNextQuestion}>Next</button>
            <div className="index">
                {currentQuestionIndex + 1} of {questions.length} questions
            </div>
            <div className="timer">Time left: {timeLeft}s</div>
        </div>
    );
}

export default Quiz;