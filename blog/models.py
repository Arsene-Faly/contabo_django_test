from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    ROLE_CHOICES = [
        ('user', 'Utilisateur'),
        ('admin', 'Administarteur')
    ]
    
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="Role"
    )
    
    name = models.CharField(
        max_length=20,
        choices=ROLE_CHOICES,
        default="user"
    )
    
    def __str__(self):
        return f"{self.user.email} - {self.name}"
    
    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

# Create your models here.
class Category(models.Model):

    name = models.CharField(max_length=150, verbose_name="Nom de la categorie")
    description = models.TextField()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
    
class Article(models.Model):
    titre = models.CharField(max_length=150, verbose_name="Titre Article")
    status = models.CharField(max_length=150, verbose_name="status")
    resume = models.TextField()
    contenu = models.TextField()
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="articles", verbose_name="Categorie" 
    )
    
    image = models.ImageField(
        upload_to="Articles/", blank=True, null=True, verbose_name="Image "
    )
    
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
    
    def __str__(self):
        return f"{self.titre}"