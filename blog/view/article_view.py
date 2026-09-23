from django.shortcuts import render, redirect
from ..models import Article, Category
from ..decorators import admin_required

@admin_required
def article_index_view(request):
    articles = Article.objects.all()
    
    context = {
        'page' : 'article',
        'articles' : articles
    }
    return render(request, 'pages/admin/articles/list.html', context)

@admin_required
def article_detail_view(request, id):
    article = Article.objects.filter(id=id).exists()
    
    if article:
        article = Article.objects.get(id=id)
    else:
        return redirect("article_index")
    
    context = {
        'page' : 'article',
        'article' : article
    }
    
    return render(request, 'pages/admin/articles/detail.html', context)

@admin_required
def article_create_view(request):

    categories = Category.objects.all()

    status = ["Brouillon", "Publié"]

    errors = []
    success = []

    title = ''
    category = ''
    status_select = ''
    resume = ''
    contenu = ''
    image = None

    if request.method == 'POST':

        title = request.POST.get('title', '').strip()
        category = request.POST.get('category', '').strip()
        status_select = request.POST.get('status', '').strip()
        resume = request.POST.get('resume', '').strip()
        contenu = request.POST.get('contenu', '').strip()
        image = request.FILES.get("image")

        # ==========================
        # VALIDATION
        # ==========================

        if not title:
            errors.append("Titre obligatoire")
        elif len(title) < 5:
            errors.append("Le titre doit contenir au moins 5 caractères")
        elif len(title) > 150:
            errors.append("Le titre ne doit pas dépasser 150 caractères")

        if not category:
            errors.append("Veuillez choisir une catégorie")
        else:
            try:
                category_obj = Category.objects.get(id=category)
            except Category.DoesNotExist:
                errors.append("La catégorie sélectionnée n'existe pas")

        if not status_select:
            errors.append("Veuillez choisir un statut")
        elif status_select not in status:
            errors.append("Le statut sélectionné est invalide")

        if not resume:
            errors.append("Le résumé est obligatoire")
        elif len(resume) < 10:
            errors.append("Le résumé doit contenir au moins 10 caractères")

        if not contenu:
            errors.append("Le contenu est obligatoire")
        elif len(contenu) < 20:
            errors.append("Le contenu doit contenir au moins 20 caractères")

        # ==========================
        # VALIDATION IMAGE
        # ==========================

        if image:

            allowed_extensions = ['jpg', 'jpeg', 'png', 'webp']

            extension = image.name.split('.')[-1].lower()

            if extension not in allowed_extensions:
                errors.append(
                    "L'image doit être au format JPG, JPEG, PNG ou WEBP"
                )

            # 2 Mo maximum
            if image.size > 2 * 1024 * 1024:
                errors.append(
                    "L'image ne doit pas dépasser 2 Mo"
                )

        # ==========================
        # CREATION ARTICLE
        # ==========================

        if not errors:

            Article.objects.create(
                titre=title,
                status=status_select,
                resume=resume,
                contenu=contenu,
                category=category_obj,
                image=image
            )

            success.append("Article créé avec succès")

            return redirect('article_index')

        print(errors)

    context = {
        'page': 'article',
        'categories': categories,
        'status': status,
        'title': title,
        'category': category,
        'status_select': status_select,
        'resume': resume,
        'contenu': contenu,
        'errors': errors,
        'success': success,
    }

    return render(
        request,
        'pages/admin/articles/create.html',
        context
    )

@admin_required
def article_edit_view(request):
    context = {
        'page' : 'article'
    }
    return render(request, 'pages/admin/articles/edit.html', context)

@admin_required
def article_delete_view(request):
    context = {
        'page' : 'article'
    }
    return render(request, 'pages/admin/articles/delete.html', context)