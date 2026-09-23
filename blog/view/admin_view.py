from django.shortcuts import render
from ..decorators import admin_required

@admin_required
def admin_view(request):
    context = {
        'page' : 'dashboard'
    }
    return render(request, 'pages/admin/index.html', context)