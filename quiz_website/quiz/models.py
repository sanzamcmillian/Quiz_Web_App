from django.contrib.auth.models import AbstractUser, Group, Permission
import uuid
from django.db import models

from django.db import models
import uuid

class BaseModel(models.Model):
    """
    Abstract base model providing common fields for all models.

    Attributes:
        uid (UUIDField): A universally unique identifier (UUID) as the primary key.
        created_at (DateField): The date and time the record was created, auto-generated.
        updated_at (DateField): The date and time the record was last updated, auto-generated.
    """
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser):
    """
    Custom User model extending Django's AbstractUser.
    """
    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    groups = models.ManyToManyField(
        Group,
        related_name='custom_user_set',  # Change this to avoid conflicts
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='custom_user_permissions_set',  # Change this to avoid conflicts
        blank=True,
    )



class Topic(BaseModel):
    """
    Model representing a topic or category for quizzes.

    Attributes:
        name (CharField): The name of the topic.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Returns a string representation of the Topic instance.

        Returns:
            str: The name of the topic.
        """
        return self.name


class Quiz(BaseModel):
    """
    Model representing a quiz.

    Attributes:
        title (CharField): The title of the quiz.
        description (TextField): A detailed description of the quiz.
        topics (ManyToManyField): The topics related to the quiz.
    """
    title = models.CharField(max_length=255)
    description = models.TextField()
    topics = models.ManyToManyField(Topic, related_name="quizzes")

    def __str__(self):
        """
        Returns a string representation of the Quiz instance.

        Returns:
            str: The title of the quiz.
        """
        return self.title


class Question(BaseModel):
    """
    Model representing a question in a quiz.

    Attributes:
        MULTIPLE_CHOICE (str): Identifier for multiple-choice question type.
        TRUE_FALSE (str): Identifier for true/false question type.
        QUESTION_TYPES (list): A list of tuples representing the available question types.
        quiz (ForeignKey): The quiz that the question belongs to.
        question_text (CharField): The text of the question.
        question_type (CharField): The type of question, either multiple-choice or true/false.
    """
    MULTIPLE_CHOICE = 'MC'
    TRUE_FALSE = 'TF'
    QUESTION_TYPES = [
        (MULTIPLE_CHOICE, 'Multiple Choice'),
        (TRUE_FALSE, 'True/False'),
    ]

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(
        max_length=2, choices=QUESTION_TYPES, default=MULTIPLE_CHOICE
    )

    def __str__(self):
        """
        Returns a string representation of the Question instance.

        Returns:
            str: The text of the question.
        """
        return self.question_text


class Answer(BaseModel):
    """
    Model representing an answer to a question.

    Attributes:
        question (ForeignKey): The question this answer is related to.
        answer_text (CharField): The text of the answer.
        is_correct (BooleanField): Whether or not the answer is correct.
    """
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        """
        Returns a string representation of the Answer instance.

        Returns:
            str: The text of the answer.
        """
        return self.answer_text


class UserQuizResult(BaseModel):
    """
    Model representing a user's result for a particular quiz.

    Attributes:
        user (ForeignKey): The user who took the quiz.
        quiz (ForeignKey): The quiz that was taken.
        score (IntegerField): The user's score on the quiz.
        date_taken (DateField): The date when the quiz was taken.
    """
    user = models.ForeignKey(User, related_name='quiz_results', on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, related_name='quiz_results', on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateField()

    def __str__(self):
        """
        Returns a string representation of the UserQuizResult instance.

        Returns:
            str: A string combining the user's username, quiz title, and score.
        """
        return f"{self.user.username} - {self.quiz.title} - {self.score}"