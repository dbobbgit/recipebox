from django.contrib import admin


from recipe_app.models import Recipe, Author
# Register your models here.

admin.site.register(Author)
admin.site.register(Recipe)