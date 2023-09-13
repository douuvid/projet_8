from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def inscription(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Inscription réussie !')
            return redirect('login')  # Supposez qu'après une inscription réussie, vous redirigez l'utilisateur vers la page de connexion.
        else:
            messages.error(request, 'Erreur lors de l\'inscription. Veuillez vérifier les informations fournies.')
    else:
        form = UserCreationForm()
    return render(request, 'logging_template.html', {'form': form})




