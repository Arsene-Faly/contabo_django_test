from django.contrib import admin
from .models import Category, Article, Role

class AdminCategory(admin.ModelAdmin):
    list_display = ("id", "name", "description")

# Register your models here.
admin.site.register(Category, AdminCategory)

class AdminArticle(admin.ModelAdmin):
    list_display = ("id", "titre", "status", "resume", "contenu", "category")

# Register your models here.
admin.site.register(Article, AdminArticle)

class AdminRole(admin.ModelAdmin):
    list_display = ("id", "user", "name")
    
admin.site.register(Role, AdminRole)