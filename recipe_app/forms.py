from django import forms
from recipe_app.models import Author
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create two forms: RecipeForm & AuthorForm
"""
Author:
    - Name: CharField
    - Bio: TextField

Recipe:
    - Title: CharField
    - Author: ForeignKey
    - Description: TextField
    - Time Required: CharField (for example, "One hour")
    - Instructions: TextField
"""

class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
            'name', 
            'bio'
        ]

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=500)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]