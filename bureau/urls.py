from django.urls import path

from bureau.views import administrationPage, bureauPage


# Création de liens de pages.

urlpatterns = [
    path('', bureauPage, name='bureau'), # Lien de la page du bureau.
    path('admin/', administrationPage, name='admin'), # Lien de la page d'administration'.
]