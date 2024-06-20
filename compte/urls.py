from django.urls import path
from django.contrib.auth import views

from .views import inscriptionPage

urlpatterns = [
    path('inscription/', inscriptionPage, name='inscrire'),
    path('connexion/', views.LoginView.as_view(template_name='compte/connexion.html', redirect_authenticated_user=False), name='connecte'),
    path('connexion/', views.LogoutView.as_view(), name='deconnecte'),
]