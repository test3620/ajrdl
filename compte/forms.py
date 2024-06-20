from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from phonenumber_field.widgets import PhoneNumberPrefixWidget


class MembreForm(UserCreationForm):
    """
    Un formulaire personnalisé pour créer de nouveaux utilisateurs.
    """

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Mot de passe'            
            }),
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirmation' 
            }),
    ) 

    class Meta:
        model = get_user_model()
        fields = [
            'last_name',
            'first_name', 
            'email',
            'contact',
            'ville',
            'quartier',
            'profession',
            'naissance',
            'photo',
            ]
        
        widgets = {  # Widgets des champs du model 'Membre'
         # Nom
         'last_name': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Nom'
            }
         ),

         # Prénom
         'first_name': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Prénom'
            }
         ),

         # Profession
         'profession': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Profession'
            }
         ),

         # Email
         'email': forms.EmailInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Email'
            }
         ),
         
         # Ville résidentielle
         'ville': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Ville habitée'
            }
         ),

         # Quartier
         'quartier': forms.TextInput(
            attrs={
               'class': 'form-control',
               'placeholder': 'Quartier'
            }
         ),

         # Contact
         'contact': PhoneNumberPrefixWidget( 
            initial="TO",
            attrs={
               'class': 'form-control flex-fill',
               'placeholder': '91180391'
            }
         ),

         # Date de naissance
         'naissance': forms.SelectDateWidget(
            years=(1950, 1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024),
            attrs={
               'class':'form-control'
            }
         ),

         # Image
         'photo': forms.FileInput(
            attrs={
               'class': 'form-control',
               'placeholder': "Photo"
            }
         ),
      }