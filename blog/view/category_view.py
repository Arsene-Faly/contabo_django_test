from django.shortcuts import render, redirect
from ..models import Category
from blog.validators.validate_category import validate_category
from ..decorators import admin_required

@admin_required
def category_index_view(request):
    categories = Category.objects.all()

    context = {"page": "category", "categories": categories}
    return render(request, "pages/admin/categories/list.html", context)

@admin_required
def category_detail_view(request, id):
    category = Category.objects.filter(id=id).exists()

    if category:
        category = Category.objects.get(id=id)
    else:
        return redirect("category_index")

    context = {"page": "category", "category": category}
    return render(request, "pages/admin/categories/detail.html", context)

@admin_required
def category_create_view(request):
    errors = []
    success = []

    name = ""
    description = ""

    if request.method == "POST":
        name = request.POST.get("name").strip()
        description = request.POST.get("description").strip()

        errors = validate_category(name, description)

        if not errors:
            # print('Success')
            Category.objects.create(name=name, description=description)

            success.append("Categorie crée avec succées")
        else:
            print("Erreur")

    context = {
        "page": "category",
        "errors": errors,
        "success": success,
        "name": name,
        "description": description,
    }
    return render(request, "pages/admin/categories/create.html", context)

@admin_required
def category_edit_view(request, id):
    category = Category.objects.filter(id=id).exists()

    if category:
        category = Category.objects.get(id=id)
    else:
        return redirect("category_index")

    errors = []
    success = []

    name = category.name
    description = category.description
    
    if request.method == "POST":
        name = request.POST.get("name").strip()
        description = request.POST.get("description").strip()
    
        errors = validate_category(name, description, id)
    
        if not errors:
            # print('Success')
            category.name = name
            category.description = description
            
            category.save()

            success.append("Categorie modifé avec succées")
        else:
            print("Erreur")

    context = {
        "page": "category",
        "errors": errors,
        "success": success,
        "name": name,
        "description": description,
    }
    
    return render(request, "pages/admin/categories/edit.html", context)

@admin_required
def category_delete_view(request, id):
    category = Category.objects.filter(id=id).exists() #renvoie true or false

    if category:
    # condition en recuperant si c'est vrai ou faux l'exixtance de categorie
        category = Category.objects.get(id=id)
    else:
        return redirect("category_index")

    if request.method == "POST":
        category.delete()
        return redirect("category_index")

    context = {"page": "category", "category": category}
    return render(request, "pages/admin/categories/delete.html", context)
