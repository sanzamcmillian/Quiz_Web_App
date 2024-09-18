from django.shortcuts import render, redirect
from .services import get_questions
from .forms import QuizForm
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


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """Handle user login."""
    email = request.data.get('email')
    password = request.data.get('password')
    
    user = authenticate(request, username=email, password=password)
    
    if user is not None:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key}, status=status.HTTP_200_OK)
    return Response({'message': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny]) #Allow access to this views for unathenticated users
def register_view(request):
    """Handle user registration."""
    name = request.data.get('name')
    surname = request.data.get('surname')
    email = request.data.get('email')
    password = request.data.get('password')
    
    if User.objects.filter(username=email).exists():
        return Response({'message': 'User already exists'}, status=status.HTTP_400_BAD_REQUEST)
    
    user = User.objects.create_user(username=email, password=password, first_name=name, last_name=surname)
    return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def logout_view(request):
    """Handle user logout."""
    request.user.auth_token.delete()  # Delete the token
    logout(request)
    return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)

def home_view(request):
    # List of quiz categories or topics
    categories = [
        "General Knowledge", "Science",
        "History", "Entertainment", "Mythology",
        "Sports", "Celebrities", "Animals",
        "Vehicles", "Politics"
    ]
    return render(request, 'home.html', {'categories': categories})

def quiz_detail_view(request, category):
    # Display details about the quiz and a start button
    return render(request, 'quiz_detail.html', {'category': category})

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
    # Retrieve the score from query parameters
    score = request.GET.get('score', None)
    if score is not None:
        try:
            score = int(score)
        except ValueError:
            score = None
    
    return render(request, 'result.html', {'score': score})
