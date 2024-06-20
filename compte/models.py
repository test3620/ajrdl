from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class CustomUserManager(BaseUserManager):
    """
    Définissez un gestionnaire de modèles pour le modèle utilisateur sans champ de 
    nom d'utilisateur.
    """

    def _create_user(self, email, password=None, **extra_fields):
        """
        Créez et enregistrez un utilisateur avec l'e-mail et le mot de passe donnés.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Créez et enregistrez un superutilisateur avec l'e-mail et le mot de passe donnés.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

# COMPTE DE MEMBRE 
class Membre(AbstractUser):
    username = None

    contact = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    ville = models.CharField(max_length=50)
    quartier = models.CharField(max_length=50)
    profession = models.CharField(max_length=50)
    naissance = models.DateField(default='1960-01-01')
    photo = models.ImageField(default='default.jpg', upload_to='membre/identite', height_field=None, width_field=None, max_length=None)
    adhesion = models.DateField(auto_now=False, auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.last_name   
    
# ADHÉSION   
class MonAdhesion(models.Model): # Adhésion.
    membre = models.OneToOneField("compte.Membre", on_delete=models.CASCADE)
    montant = models.IntegerField()
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)

# MENSUEL
class Mensuel(models.Model): # Mensuel.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50, default='Rond point Kpogli')
    paye = models.BooleanField(default=False)

def __str__(self):
    return f"Mensuel de {self.membre.last_name} {self.membre.first_name}"

# NAISSANCE
class NouveauNe(models.Model): # Naissance.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    enfant = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)

# RÉJOUISSANCE
class Rejouissance(models.Model): # Réjouissance.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    lieu = models.CharField(max_length=50)
    paye = models.BooleanField(default=False)

# DON
class Don(models.Model): # Don.
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    objet = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)

# DÉCÈS
class Deces(models.Model): # Décès:
    membre = models.ForeignKey('compte.Membre', on_delete=models.CASCADE)
    montant = models.IntegerField()
    deces = models.CharField(max_length=50)
    reunion = models.DateField(auto_now=False, auto_now_add=False)
    paye = models.BooleanField(default=False)   