// src/api.js
export const fetchQuestions = async () => {
    try {
      const response = await fetch('https://opentdb.com/api.php?amount=10&type=multiple');
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error fetching questions:', error);
      throw error; // rethrow to be caught in the Quiz component
    }
  };
  