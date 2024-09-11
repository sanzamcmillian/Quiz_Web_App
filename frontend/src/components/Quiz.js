import React, { useState, useEffect, useCallback } from 'react';
import Confetti from 'react-confetti'; // For confetti animation
import './style/Quiz.css'; // Import the CSS file

const Quiz = () => {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [selectedAnswer, setSelectedAnswer] = useState('');
  const [score, setScore] = useState(0);
  const [isFinished, setIsFinished] = useState(false);
  const [showAnswers, setShowAnswers] = useState(false);
  const [timer, setTimer] = useState(30); // Timer state
  const [intervalId, setIntervalId] = useState(null);
  const [incorrectAnswers, setIncorrectAnswers] = useState([]);
  const [correctAnswers, setCorrectAnswers] = useState([]);

  useEffect(() => {
    // Fetch questions from API
    const fetchQuestions = async () => {
      try {
        const response = await fetch('https://opentdb.com/api.php?amount=10&type=multiple');
        const data = await response.json();
        setQuestions(data.results);
      } catch (error) {
        console.error('Error fetching questions:', error);
      }
    };

    fetchQuestions();
  }, []);

  useEffect(() => {
    if (timer <= 0) {
      handleNextQuestion();
    }
  }, [timer]);

  useEffect(() => {
    if (intervalId) {
      clearInterval(intervalId);
    }
    const id = setInterval(() => {
      setTimer((prev) => prev - 1);
    }, 1000);
    setIntervalId(id);
    return () => clearInterval(id);
  }, [currentQuestion]);

  const handleNextQuestion = useCallback(() => {
    if (selectedAnswer) {
      const correctAnswer = questions[currentQuestion]?.correct_answer;
      if (selectedAnswer === correctAnswer) {
        setScore((prev) => prev + 1);
      } else {
        setIncorrectAnswers((prev) => [...prev, { question: questions[currentQuestion]?.question, selectedAnswer, correctAnswer }]);
      }
      setSelectedAnswer('');
      setTimer(30); // Reset timer
      setCurrentQuestion((prev) => prev + 1);
    }
  }, [selectedAnswer, questions, currentQuestion]);

  const handleAnswerClick = (answer) => {
    setSelectedAnswer(answer);
  };

  const handleFinish = () => {
    setIsFinished(true);
    setShowAnswers(true);
    clearInterval(intervalId); // Stop the timer
  };

  if (isFinished) {
    return (
      <div className="result-container">
        {score >= 5 ? (
          <>
            <Confetti />
            <h1>Congratulations!</h1>
            <p>You scored {score} out of {questions.length}.</p>
            <button onClick={() => window.location.reload()} className="btn btn-primary">Play Again</button>
          </>
        ) : (
          <>
            <h1>Oops!</h1>
            <p>You scored {score} out of {questions.length}.</p>
            <button onClick={() => window.location.reload()} className="btn btn-primary">Play Again</button>
          </>
        )}
        {showAnswers && (
          <div className="answers-container">
            <h3>Review your answers:</h3>
            {incorrectAnswers.map((item, index) => (
              <div key={index} className="answer-review">
                <p><strong>Question:</strong> {item.question}</p>
                <p><strong>Your Answer:</strong> {item.selectedAnswer}</p>
                <p><strong>Correct Answer:</strong> {item.correctAnswer}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    );
  }

  return (
    <div className="quiz-container">
      {questions.length > 0 && currentQuestion < questions.length ? (
        <div className="question-container">
          <h2>{questions[currentQuestion]?.question}</h2>
          <div className="timer">Time Left: {timer}s</div>
          <div className="options-container">
            {[...questions[currentQuestion]?.incorrect_answers, questions[currentQuestion]?.correct_answer].map((answer, index) => (
              <button
                key={index}
                onClick={() => handleAnswerClick(answer)}
                className={`option-button ${selectedAnswer === answer ? 'selected' : ''}`}
              >
                {answer}
              </button>
            ))}
          </div>
          <button onClick={handleNextQuestion} className="btn btn-primary">Next Question</button>
          {currentQuestion === questions.length - 1 && (
            <button onClick={handleFinish} className="btn btn-primary finish-button">Finish Quiz</button>
          )}
        </div>
      ) : (
        <div className="loading">Loading questions...</div>
      )}
    </div>
  );
};

export default Quiz;