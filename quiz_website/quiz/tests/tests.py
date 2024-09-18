from django.test import TestCase
from unittest.mock import patch
from ..services import get_questions
# Create your tests here.


class QuizServiceTest(TestCase):
    """class to test third party APIS """
    @patch('quiz.services.requests.get')
    def test_get_questions(self, mock_get):
        """test using mock for method get"""
        mock_data = {
            "response_code": 0,
            "results": [
                {
                    "question": "What is the capital of France?",
                    "correct_answer": "Paris",
                    "incorrect_answers": ["London", "Berlin", "Rome"]
                }
            ]
        }
        
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = mock_data
        
        questions = get_questions(category='9')
        
        self.assertIsNotNone(questions)
        self.assertEqual(len(questions), 1)
        self.assertEqual(questions[0]['question'], "What is the capital of France?")
        self.assertEqual(questions[0]['correct_answer'], "Paris")
        
    @patch('quiz.services.requests.get')
    def test_get_questions_api(self, mock_get):
        """tests for api failure"""
        mock_get.return_value.status_code = 500
        
        questions = get_questions(category="9")
        
        self.assertEqual(questions, [])

