from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField( max_length=50)
    recipe_price = models.IntegerField()
    date = models.DateField(auto_now_add=True)


class Pic(models.Model):
    image = models.ImageField(upload_to='Pictures')
