from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages
from .form import CustomUserCreationForm

from django.shortcuts import render
from .models_extra import Book




def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie ! Vous pouvez maintenant vous connecter.')
            return redirect('sommaire')
        else:
            messages.error(request, 'Il y a eu une erreur avec votre inscription.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



def book_list(request):
    books = Book.objects.all()
    return render(request, 'authentification/book_list.html', {'books': books})
