from django.shortcuts import render, reverse, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import AddAuthorForm, AddRecipeForm, CreateUserForm


def index(req):
    recipes = Recipe.objects.all()
    return render(req, 'index.html', {'recipes': recipes})

def recipe_detail(req, recipe_id: int):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(req, 'recipe_detail.html', {'recipe': recipe})

def author_detail(req, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_recipes = Recipe.objects.filter(author=my_author)
    print(author_recipes[0].author) 
    return render(req, 'author_detail.html', {'author': my_author, 'recipes': author_recipes})

@login_required
def add_recipe(req):
    html = 'generic_form.html'

    if req.method == 'POST':
        form = AddRecipeForm(req.POST)
        if form.is_valid():
            data = form.cleaned_data
            Recipe.objects.create(
                title = data['title'],
                author = data['author'],
                description = data['description'],
                time_required = data['time_required'],
                instructions = data['instructions']
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = AddRecipeForm()

    return render(req, html, {'form': form})

def add_author(req):
    html = 'generic_form.html'

    if req.method == 'POST':
        form = AddAuthorForm(req.POST)
        form.save()
        return HttpResponseRedirect(reverse("homepage"))

    form = AddAuthorForm()

    return render(req, html, {'form': form})

def login_view(req):
    form = CreateUserForm()

    if req.method == 'POST':
        form = CreateUserForm(req.POST)
        if form.is_valid():
            form.save()

    return render(req, 'register.html', {'form': form})
