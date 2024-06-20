from django.shortcuts import render

from .models import Actualite

# Création de pages webs.

def actualitePage(request): # Page d'actualité.
    actualite = Actualite.objects.all()
    derniers_articles = Actualite.objects.order_by('-date')[:5]
    return render(request, 'actualite/actualite.html', {'actualite':actualite, 'derniers_articles':derniers_articles})

def detailPage(request, pk): # Page de détail des actualités.
    actualite = Actualite.objects.get(id=pk)
    derniers_articles = Actualite.objects.order_by('-date')[:5]
    return render(request, 'actualite/detail.html', {'actualite':actualite, 'derniers_articles':derniers_articles})