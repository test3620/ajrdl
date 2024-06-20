from django.urls import path

from .views import actualitePage, detailPage

# Création de liens de pages.

urlpatterns = [
    path('', actualitePage, name='actualite'), # Lien de la page d'actualité.
    path('detail/<str:pk>/', detailPage, name='detail'), # Lien de la page de detail des actualités.
]