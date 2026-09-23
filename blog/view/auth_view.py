from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from blog.models import Role
from django.contrib import messages
import re

from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    errors = []
    email = ''
    password = ''
    
    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=email,
            password=password
        )
        
        if user is not None:
            # Création session
            login(request, user)

            role = Role.objects.get(user=user)
            
            if role.name == "admin":
                return redirect("admin_dashboard")
            else:
                return redirect("login")
        
        else:
            errors.append("Email ou mot de passe incorrect")
    
    context = {
        'errors': errors,
    }
    
    return render(request, "pages/auth/login.html", context)


def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    
    errors = []
    success = []
    email = ""
    password = ""
    password2 = ""

    if request.method == "POST":
        email = request.POST.get("email", "").strip()
        password = request.POST.get("password", "")
        password2 = request.POST.get("confirm_password", "")

        # Validation email
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

        if not email:
            errors.append("L'email est obligatoire.")
        elif not re.match(email_regex, email):
            errors.append("L'adresse email n'est pas valide.")
            
        if User.objects.filter(email=email).exists():
            errors.append("Email existe déja")

        # Mot de passe obligatoire
        if not password:
            errors.append("Le mot de passe est obligatoire.")

        # Confirmation obligatoire
        if not password2:
            errors.append("La confirmation du mot de passe est obligatoire.")

        # Vérifier la longueur seulement si le mot de passe existe
        if password and len(password) < 6:
            errors.append("Le mot de passe doit contenir au moins 6 caractères.")

        # Comparer seulement si les deux sont renseignés
        if password and password2 and password != password2:
            errors.append("Les mots de passe ne correspondent pas.")
            
        if not errors:
            user = User.objects.create_user(
                username=email,
                email=email,
                password=password
            )
            
            # Créer role automatique
            Role.objects.create(
                user=user,
                name='user'
            )
            
            messages.success(
                request,
                "Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter."
            )
            
            return redirect('login')
            
            

    context = {
        "errors": errors,
        "success": success,
        "email": email,
    }

    return render(request, "pages/auth/register.html", context)

def logout_view(request):

    logout(request)

    return redirect("home")