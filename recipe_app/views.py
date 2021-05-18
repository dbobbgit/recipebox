from django.shortcuts import render, reverse, HttpResponseRedirect

# Create your views here.
from recipe_app.models import Author, Recipe
from recipe_app.forms import AddAuthorForm, AddRecipeForm
from django.contrib.auth.forms import UserCreationForm

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'index.html', {'recipes': recipes})

def recipe_detail(request, recipe_id: int):
    recipe = Recipe.objects.get(id=recipe_id)
    return render(request, 'recipe_detail.html', {'recipe': recipe})

def author_detail(request, author_id: int):
    my_author = Author.objects.get(id=author_id)
    author_recipes = Recipe.objects.filter(author=my_author)
    print(author_recipes[0].author) 
    return render(request, 'author_detail.html', {'author': my_author, 'recipes': author_recipes})

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

def register(req):
    form = UserCreationForm()
    return render(req, 'register.html', {'form': form})
    
