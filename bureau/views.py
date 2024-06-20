from django.shortcuts import render

from .models import Bureau

# Création de pages webs.

def bureauPage(request): # Page du bureau.
    bureau = Bureau.objects.all()
    return render(request, 'bureau/bureau.html', {'bureau':bureau})

def administrationPage(request): # Page d'administration.
    return render(request, 'bureau/admin.html')