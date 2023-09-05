from django.http import HttpResponse
from django.shortcuts import render



def creer_ticket(request):
    return render(request, 'creer_ticket.html')
