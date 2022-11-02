from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Creamos un formulario nuevo que hereda del formulario UserCreationForm y lr agregamos los campos que queremos solicitar:
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': ''}))
    first_name = forms.CharField(required=True, label= 'Nombre')
    last_name = forms.CharField(required=True, label= 'Apellido')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2')

    #clean email field
    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            User._default_manager.get(email=email)
        except User.DoesNotExist:
            return email
        raise forms.ValidationError('Email duplicado')