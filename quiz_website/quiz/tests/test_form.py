import pytest
from django import forms
from django.contrib.auth.models import User
from django.test import TestCase
from ..forms import RegisterForm, QuizForm

class TestRegisterForm(TestCase):

    def test_register_form_valid_data(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        assert form.is_valid()

    def test_register_form_missing_email(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123'
        })
        assert not form.is_valid()
        assert 'email' in form.errors

    def test_register_form_password_mismatch(self):
        form = RegisterForm(data={
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'complexpassword123',
            'password2': 'differentpassword123'
        })
        assert not form.is_valid()
        assert 'password2' in form.errors

class TestQuizForm(TestCase):

    def test_quiz_form_valid_data(self):
        questions = [
            {
                'question': 'What is the capital of France?',
                'correct_answer': 'Paris',
                'incorrect_answers': ['London', 'Berlin', 'Madrid']
            },
            {
                'question': 'What is 2 + 2?',
                'correct_answer': '4',
                'incorrect_answers': ['3', '5', '6']
            }
        ]
        form_data = {
            'question_1': 'Paris',
            'question_2': '4'
        }
        form = QuizForm(data=form_data, questions=questions)
        assert form.is_valid()
        assert form.calculate_score() == 2

    def test_quiz_form_invalid_data(self):
        questions = [
            {
                'question': 'What is the capital of France?',
                'correct_answer': 'Paris',
                'incorrect_answers': ['London', 'Berlin', 'Madrid']
            },
            {
                'question': 'What is 2 + 2?',
                'correct_answer': '4',
                'incorrect_answers': ['3', '5', '6']
            }
        ]
        form_data = {
            'question_1': 'London',
            'question_2': '5'
        }
        form = QuizForm(data=form_data, questions=questions)
        assert form.is_valid()
        assert form.calculate_score() == 0

    def test_quiz_form_missing_data(self):
        questions = [
            {
                'question': 'What is the capital of France?',
                'correct_answer': 'Paris',
                'incorrect_answers': ['London', 'Berlin', 'Madrid']
            }
        ]
        form_data = {}
        form = QuizForm(data=form_data, questions=questions)
        assert not form.is_valid()
        assert 'question_1' in form.errors