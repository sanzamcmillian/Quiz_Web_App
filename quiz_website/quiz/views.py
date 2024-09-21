from django.shortcuts import render, redirect
from .services import get_questions
from .forms import QuizForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny


def landing_view(request):
    """method to render home page"""
    return render(request, 'index.html')


def home_view(request):
    """List of quiz categories or topics"""
    categories = [
        "General Knowledge", "Science",
        "History", "Entertainment", "Mythology",
        "Sports", "Celebrities", "Animals",
        "Vehicles", "Politics"
    ]
    return render(request, 'quiz_detail.html', {'categories': categories})


def register_view(request):
    """auth to handle user registration"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in automatically after registration
            login(request, user)
            return redirect('quiz_detail')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    """auth to handle login for user"""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('quiz_detail')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    """Handle user logout."""
    request.user.auth_token.delete()
    logout(request)
    return Response(
        {'message': 'Logged out successfully'},
        status=status.HTTP_200_OK
        )


def quiz_view(request, category):
    """Fetch quiz questions from an external API and handle form submission"""
    questions = get_questions(num_questions=5)

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = form.calculate_score()
            # Use query parameters to pass the score
            return redirect(f'{reverse("result")}?score={score}')
    else:
        form = QuizForm(questions=questions)

    context = {
        'form': form,
        'questions': questions,
    }
    return render(request, 'quiz_view.html', context)


def result_view(request):
    """Retrieve the score from query parameters"""
    score = request.GET.get('score', None)
    if score is not None:
        try:
            score = int(score)
        except ValueError:
            score = None

    return render(request, 'result.html', {'score': score})
