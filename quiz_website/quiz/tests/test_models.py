import pytest
from django.contrib.auth.models import User
from quiz.models import QuizResult, UserResponse, Leaderboard
from django.utils import timezone

@pytest.mark.django_db
def test_quiz_result_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    quiz_result = QuizResult.objects.create(
        user=user,
        score=80,
        total_questions=100,
        percentage=80,
        quiz_category='Science',
        date_taken=timezone.now()
    )
    assert quiz_result.user == user
    assert quiz_result.score == 80
    assert quiz_result.total_questions == 100
    assert quiz_result.percentage == 80
    assert quiz_result.quiz_category == 'Science'
    assert quiz_result.date_taken is not None

@pytest.mark.django_db
def test_user_response_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    user_response = UserResponse.objects.create(
        user=user,
        question_text='What is the capital of France?',
        selected_option='Paris',
        correct_option='Paris',
        is_correct=True
    )
    assert user_response.user == user
    assert user_response.question_text == 'What is the capital of France?'
    assert user_response.selected_option == 'Paris'
    assert user_response.correct_option == 'Paris'
    assert user_response.is_correct is True

@pytest.mark.django_db
def test_leaderboard_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    leaderboard_entry = Leaderboard.objects.create(
        user=user,
        total_score=150.0
    )
    assert leaderboard_entry.user == user
    assert leaderboard_entry.total_score == 150.0
    assert leaderboard_entry.rank is None  # Rank is set in save method

@pytest.mark.django_db
def test_leaderboard_ranking():
    user1 = User.objects.create_user(username='user1', password='12345')
    user2 = User.objects.create_user(username='user2', password='12345')
    Leaderboard.objects.create(user=user1, total_score=200.0)
    Leaderboard.objects.create(user=user2, total_score=300.0)

    leaderboard = Leaderboard.objects.order_by('-total_score')
    assert leaderboard[0].user == user2
    assert leaderboard[0].rank == 1
    assert leaderboard[1].user == user1
    assert leaderboard[1].rank == 2