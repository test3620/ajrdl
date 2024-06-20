from django.shortcuts import render
#from django.contrib.auth import get_user_model

from compte.models import Membre # Importation du model membre.

# CREATION DE PAGES (VUES)

def accueilPage(request): # Page d'accueil.
    return render(request, 'index.html')

def membrePage(request): # Page de membres.
    membre = Membre.objects.all() # Récupérqtion de tous les membre.
    return render(request, 'membre.html', {'membre':membre})

def profilePage(request): # Page de profile d'un membre (utilisateur).
    return render(request, 'profile.html')

def contactPage(request): # Page de contact de l'AJRDL.
    return render(request, 'contact.html')