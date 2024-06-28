from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Periodista, Noticas

class PeriodistaForm(forms.ModelForm):
    class Meta:
        model = Periodista
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(help_text='Obligatorio. Proporciona una dirección de correo electrónico válida.')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            # Ejemplo de asignación de roles básica
            if user.id == 1:
                user.is_staff = True  # Asignar rol de administrador
            else:
                user.is_staff = False  # Asignar rol de usuario normal
            user.save()
        return user


class NoticiasForm(forms.ModelForm):
    class Meta:
        model = Noticas
        fields = '__all__'
