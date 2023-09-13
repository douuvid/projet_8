from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages



# Create your views here.
def register(request):
    if request.method == 'POST':
        messsage = ''
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sommaire')  # Rediriger vers la page d'accueil après l'inscription réussie
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


