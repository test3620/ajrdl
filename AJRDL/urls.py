from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import accueilPage, contactPage, membrePage, profilePage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', accueilPage, name='accueil'), # Lien de la page d'accueil.
    path('profile/', profilePage, name='profile'), # Lien de la page de profile.
    path('membre/', membrePage, name='membre'), # Lien de la page de membre.
    path('contact/', contactPage, name='contact'), # Lien de la page de contact.
    path('compte/', include('compte.urls')), # Lien de la page d'utilisateur.
    path('actualite/', include('actualite.urls')), # Lien de la page d'actualité.
    path('bureau/', include('bureau.urls')), # Lien de la page du bureau.
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
