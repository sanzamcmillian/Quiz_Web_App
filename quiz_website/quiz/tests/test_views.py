import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import Client
from quiz.models import QuizResult, Leaderboard

@pytest.fixture
def client():
    return Client()

@pytest.fixture
def user(db):
    return User.objects.create_user(username='testuser', password='password')


@pytest.mark.django_db
def test_quiz_view_get(client, user):
    client.login(username='testuser', password='password')
    response = client.get(reverse('quiz_view', args=['General Knowledge']))
    assert response.status_code == 200
    assert 'quiz_view.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_result_view(client, user):
    quiz_result = QuizResult.objects.create(
        user=user,
        score=3,
        total_questions=5,
        percentage=60,
        quiz_category='General Knowledge',
        date_taken='2023-01-01'
    )
    client.login(username='testuser', password='password')
    response = client.get(reverse('result_view', args=[quiz_result.id]))
    assert response.status_code == 200
    assert 'result.html' in [t.name for t in response.templates]

@pytest.mark.django_db
def test_leaderboard_view(client, user):
    Leaderboard.objects.create(user=user, total_score=10)
    client.login(username='testuser', password='password')
    response = client.get(reverse('leaderboard_view'))
    assert response.status_code == 200
    assert 'leaderboard.html' in [t.name for t in response.templates]