from django.shortcuts import render

from .forms import MembreForm

# Création de vues.

def inscriptionPage(request): # Page d'inscription.
    if request.method == 'POST':
        form = MembreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MembreForm()
    return render(request, 'compte/inscription.html', {'title':'Inscription', 'form':form})