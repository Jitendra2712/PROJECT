from django.contrib import admin
from .models import Recipe,Pic

# Register your models here.


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ("id", "recipe_name","recipe_price","date")


@admin.register(Pic)
class PicAdmin(admin.ModelAdmin):
    list_display = ("image",)
    
    