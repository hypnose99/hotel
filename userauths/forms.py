from django import forms
from django.contrib.auth.forms import UserCreationForm

from userauths.models import User, Profile

# Crée un formulaire appartir d'un model ici User
class UserRegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Nom et prénoms", 'class': "a custom class"}))
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Username", 'class': "a custom class"}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Adresse email ", 'class': "a custom class"}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Numéro de téléphone", 'class': "a custom class"}))
    password1 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Mot de passe", 'class': "a custom class"}))
    password2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Retaper le mot de passe", 'class': "a custom class"}))

    
    class Meta:
        model = User
        fields = ['full_name', 'username', 'phone', 'email', 'password1', 'password2']