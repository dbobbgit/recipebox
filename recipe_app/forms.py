from django import forms
from recipe_app.models import Author
from django.contrib.auth.forms import UserCreationForm


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

class AddAuthorForm(UserCreationForm):

    name = forms.CharField(max_length=100)
    bio = forms.CharField(max_length=250)
    username = forms.CharField(max_length=150)
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = None

    # class Meta:
    #     model = Author
    #     fields = [
    #         'name', 
    #         'bio'
    #     ]

class AddRecipeForm(forms.Form):
    title = forms.CharField(max_length=100)
    author = forms.ModelChoiceField(queryset=Author.objects.all())
    description = forms.CharField(max_length=500)
    time_required = forms.CharField(max_length=50)
    instructions = forms.CharField(widget=forms.Textarea)
