from django.db import models

from django.utils import timezone

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

    def __str__(self):
        """Returns the author name as a string when the Author instance is requested"""
        return self.name
    
class Recipe(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    time_required = models.CharField(max_length=50)
    instructions = models.TextField(max_length=1500)

