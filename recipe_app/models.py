from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returns the author name as a string when the Author instance is requested"""
        return self.name
    def url(self):
        return f"/author/{self.id}"

    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField(max_length=1500)

    def __str__(self):
        return self.title
    def url(self):
        return f"/recipe/{self.id}"

