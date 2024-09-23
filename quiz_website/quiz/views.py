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
from django.db import transaction


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
    """Handle user logout.
    request.user.auth_token.delete()
    logout(request)
    return Response(
        {'message': 'Logged out successfully'},
        status=status.HTTP_200_OK
        )"""
    logout(request)
    return redirect('home')


@login_required
def quiz_view(request, category):
    """Fetch quiz questions from an external API and handle form submission"""
    number_of_questions =5
    if request.method == 'POST':
        submmited_data = request.POST
        with transaction.atomic():
            correct_answer_count =0
            for key, value in submmited_data.items():
                if key.startswith('question_') and value.split(':')[0] == value.split(':')[1]:
                    correct_answer_count +=1

            # for idx, question in enumerate(questions, start=1):
            #     selected_option = form.cleaned_data.get(f'question_{idx}')
            #     print(selected_option)
            #     correct_option = question['correct_answer']
            #     is_correct = selected_option == correct_option
            #     UserResponse.objects.create(
            #         user=user,
            #         question_text=question['question'],
            #         selected_option=selected_option,
            #         correct_option=correct_option,
            #         is_correct=is_correct
            #     )
        
            quiz_result = QuizResult.objects.create(
                user=request.user,
                score=correct_answer_count,
                total_questions=number_of_questions,
                percentage=round((correct_answer_count/number_of_questions)*100),
                quiz_category=category,
                date_taken=timezone.now()
            )

            leaderboard_entry, created = Leaderboard.objects.get_or_create(user=request.user)
            leaderboard_entry.total_score = F('total_score') + correct_answer_count
            leaderboard_entry.save()

        #return redirect(reverse("result_view") + f'?score={score}&category={category}')
        return redirect('result_view', result_id=quiz_result.id)
    else:
        questions = get_questions(num_questions=number_of_questions)
        form = QuizForm(questions=questions)

    context = {
        'form': form,
        'questions': questions,
        'category': category,
    }
    return render(request, 'quiz_view.html', context)


@login_required
def result_view(request, result_id):
    """Display the score to the user"""
    try:
        quiz_result = QuizResult.objects.get(id=result_id, user=request.user)
    except QuizResult.DoesNotExist:
        return redirect('quiz_home')  # Redirect if no result is found

    context = {
        'score': quiz_result.score,
        'category': quiz_result.quiz_category,
        'total_questions': quiz_result.total_questions,
        'percentage':quiz_result.percentage,
        'date_taken': quiz_result.date_taken,
        'quiz_result': quiz_result,    
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
