from django.shortcuts import render

# Create your views here.
from recipe_app.models import Author, Recipe

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {recipes: recipes})

def recipe_detail(request, recipe_id: int):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_posts = Author.objects.filter(author=my_author)
    return render(request, 'author_detail.html', {'author': my_author, 'posts': author_posts})