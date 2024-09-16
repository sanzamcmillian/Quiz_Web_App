from django.contrib import admin
from .models import Question, Answer, Types

class AnswerAdmin(admin.StackedInline):
    """
    Inline admin class for the Answer model.
    
    Allows Answer instances to be edited inline within the Question admin panel.
    """
    model = Answer
    extra = 1  # Number of extra forms displayed for adding new answers

class QuestionAdmin(admin.ModelAdmin):
    """
    Admin class for the Question model.
    
    This class customizes the admin interface for Question, adding an inline
    for related Answer instances, search fields, list display, and filters.
    
    Attributes:
        inlines (list): A list of inline models (AnswerAdmin) to be displayed within the Question admin form.
        list_display (tuple): Fields to display in the Question list view.
        search_fields (tuple): Fields that are searchable in the admin interface.
        list_filter (tuple): Fields to filter questions in the admin panel.
    """
    inlines = [AnswerAdmin]
    list_display = ('question_text', 'question_type', 'created_at', 'updated_at')  # Fields shown in the list view
    search_fields = ('question_text',)  # Fields searchable by admin
    list_filter = ('question_type', 'created_at')  # Fields used for filtering questions

class TypesAdmin(admin.ModelAdmin):
    """
    Admin class for the Types model.
    
    This class customizes the admin interface for Types by adding search fields and list display.
    
    Attributes:
        list_display (tuple): Fields to display in the Types list view.
        search_fields (tuple): Fields that are searchable in the admin interface.
    """
    list_display = ('name', 'description')  # Fields shown in the list view
    search_fields = ('name', 'description')  # Fields searchable by admin

class AnswerModelAdmin(admin.ModelAdmin):
    """
    Admin class for the Answer model.
    
    This class customizes the admin interface for Answer, adding search fields, list display, and filters.
    
    Attributes:
        list_display (tuple): Fields to display in the Answer list view.
        search_fields (tuple): Fields that are searchable in the admin interface.
        list_filter (tuple): Fields to filter answers in the admin panel.
    """
    list_display = ('answer_text', 'is_correct', 'question', 'created_at')  # Fields shown in the list view
    search_fields = ('answer_text', 'question__question_text')  # Enable search by answer text and question text
    list_filter = ('is_correct', 'question__question_type', 'created_at')  # Enable filters for answer correctness and related question type

# Register the models with the customized admin configurations
admin.site.register(Types, TypesAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerModelAdmin)
