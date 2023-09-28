
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import Billet

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')  
        
        
class BilletForm(forms.ModelForm):
    class Meta:
        model = Billet
        fields = ['titre', 'contenu']
