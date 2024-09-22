from django.shortcuts import render, redirect, get_object_or_404
from .services import get_questions
from .forms import QuizForm
from .models import QuizResult, UserResponse, Leaderboard
from django.utils import timezone
from django.db.models import F, Sum
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


@login_required
def quiz_view(request, category):
    """Fetch quiz questions from an external API and handle form submission"""
    questions = get_questions(num_questions=5)

    if request.method == 'POST':
        form = QuizForm(request.POST, questions=questions)
        if form.is_valid():
            score = form.calculate_score()
            total_questions = len(questions)
            user = request.user

            for idx, question in enumerate(questions):
                selected_option = form.cleaned_data.get(f'question_{idx}')
                correct_option = question['correct_answer']
                is_correct = selected_option == correct_option
                UserResponse.objects.create(
                    user=user,
                    question_text=question['question'],
                    selected_option=selected_option,
                    correct_option=correct_option,
                    is_correct=is_correct
                )
            
            quiz_result = QuizResult.objects.create(
                user=user,
                score=score,
                total_questions=total_questions,
                quiz_category=category,
                date_taken=timezone.now()
            )

            leaderboard_entry, created = Leaderboard.objects.get_or_create(user=user)
            leaderboard_entry.total_score = F('total_score') + score
            leaderboard_entry.save()
            """
            all_leaderboard = Leaderboard.objects.order_by('-total_score')
            for rank, entry in enumerate(all_leaderboard, start=1):
                entry.rank = rank
                entry.save()"""

            #return redirect(reverse("result_view") + f'?score={score}&category={category}')
            return redirect('result_view', resuld_id=quiz_result.id)
    else:
        form = QuizForm(questions=questions)

    context = {
        'form': form,
        'questions': questions,
        'category': category,
    }
    return render(request, 'quiz_view.html', context)


@login_required
def result_view(request):
    """Display the score to the user"""
    score = request.GET.get('score')
    category = request.GET.get('category')
    try:
        score = int(score)
    except (TypeError, ValueError):
        score = 0

    context = {
        'score': score,
        'category': category,
    }
    

    return render(request, 'result.html', context)


@login_required
def leaderboard_view(request):
    """Display the leaderboard to the user
    top_users = Leaderboard.objects.order_by('rank')[:10]
    context = {
        'top_users': top_users
    }
    return render(request, 'leaderboard.html', context)"""
    leaderboard = Leaderboard.objects.annotate(
        total=Sum('total_score')
    ).order_by('-total')[:10]

    for idx, entry in enumerate(leaderboard, start=1):
        entry.rank = idx
        entry.save()

    context = {
        'leaderboard': leaderboard,
    }
    return render(request, 'leaderboard.html', context)
