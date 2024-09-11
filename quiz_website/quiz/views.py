from django.shortcuts import render, redirect
from .services import get_questions
from .forms import QuizForm
# Create your views here.
#request -> response
# quiz/views.py
from quiz.models import Quiz
from django.http import HttpResponse


def test_view(request):
    return HttpResponse("Test view works!")

def home_view(request):
    # In this case, you might dynamically generate a list of quiz categories or topics
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
    """fetch quiz questions from external API"""
    questions = get_questions(num_questions=5)
    context = {'questions': questions}
    return render(request, 'quiz_view.html', context)


def result_view(request, score):
    # Display the user's score and correct answers
    return render(request, 'result.html', {'score': score})
