from socket import fromshare
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from AppMeteo.models import Avatar 



class FenomenoFormulario(forms.Form):
    fenomeno=forms.CharField()
    fecha=forms.DateField()


class MiembroFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    edad = forms.IntegerField()


class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]



class FormularioEditar(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir Contraseña", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name", "password1", "password2"]




class AvatarFormulario(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen"]


