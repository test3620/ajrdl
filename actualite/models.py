from django.db import models
from django.utils import timezone

# Céation de model.

class Actualite(models.Model): # Model d'actualité.
    titre = models.CharField(max_length=100)
    contenu = models.TextField()
    image = models.ImageField(upload_to='actualite', height_field=None, width_field=None, max_length=None)
    date = models.DateTimeField(default=timezone.now)
    auteur = models.ForeignKey("compte.Membre", on_delete=models.CASCADE)

    def __str__(self):
        return self.titre
    