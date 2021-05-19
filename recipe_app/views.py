from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .models import Author, Recipe
from .forms import AddAuthorForm, AddRecipeForm
from django.contrib.auth.models import User


# Create your views here.
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

@login_required
@staff_member_required
def add_author(req):
    
    html = 'new_user.html'

    if req.method == 'POST':
        form = AddAuthorForm(req.POST)
        if form.is_valid():
            # form.save()
            data = form.cleaned_data
            my_user = User.objects.create_user(
                username=data['username'], 
                password=data['password1']
                )
            Author.objects.create(
                name=data['name'], 
                bio=data['bio'],
                user = my_user
                )
            return HttpResponseRedirect(reverse('homepage'))

    form = AddAuthorForm()

    return render(req, html, {'form': form})

def login_view(req):

    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        
        user = authenticate(req, username=username, password=password)

        if user:
            login(req, user)
            if 'next' in req.POST:
                return HttpResponseRedirect(req.POST.get('next'))
            else:
                return HttpResponseRedirect(reverse('homepage'))
                

    next = req.GET.get('next', '')
    context = {'next': next}
    return render(req, 'login.html', context)

@login_required
def user_logout(req):
    logout(req)
    return HttpResponseRedirect(reverse('homepage'))
    