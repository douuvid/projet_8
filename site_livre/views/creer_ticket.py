from django.http import HttpResponse
from django.shortcuts import render
from django.contrib import messages



def creer_ticket(request):
    #si le ticket a ete fait Ticket reussit  
    messages.success(request,"Ticket reussit !")
    return render(request, 'creer_ticket.html')
