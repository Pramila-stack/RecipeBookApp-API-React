from django.db import models

# Create your models here.

# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    ingredients = models.TextField()
    steps = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    

    