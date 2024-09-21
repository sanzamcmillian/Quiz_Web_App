from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add an email field if needed

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class QuizForm(forms.Form):
    def __init__(self, *args, **kwargs):
        questions = kwargs.pop('questions', [])
        super(QuizForm, self).__init__(*args, **kwargs)

        for i, question in enumerate(questions):
            field_name = f'question_{i}'
            self.fields[field_name] = forms.ChoiceField(
                label=question['question'],
                choices=[(ans, ans) for ans in question['incorrect_answers'] + [question['correct_answer']]],
                widget=forms.RadioSelect,
                required=True
            )
            self.fields[field_name].question = question  # Attach question data to the field

    def calculate_score(self):
        correct_answers = 0
        for field_name, field_value in self.cleaned_data.items():
            question = self.fields[field_name].question
            if field_value == question['correct_answer']:
                correct_answers += 1
        return correct_answers
