from django.shortcuts import redirect, render
from django.contrib import messages
from .form import CustomUserCreationForm, BilletForm
from site_livre.models import Book
from .models import Billet

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie ! Vous pouvez maintenant vous connecter.')
            return redirect('sommaire')
        else:
            messages.error(request, 'Il y a eu une erreur avec votre inscription: ' + ', '.join(form.errors))
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'authentification/book_list.html', {'books': books})

def ajouter_billet(request):
    if request.method == "POST":
        form = BilletForm(request.POST)
        if form.is_valid():
            billet = form.save(commit=False)
            billet.auteur = request.user
            billet.save()
            return redirect('summary')
    else:
        form = BilletForm()
    return render(request, 'ajouter_billet.html', {'form': form})

def home(request):
    return render(request, 'acceuil.html')
