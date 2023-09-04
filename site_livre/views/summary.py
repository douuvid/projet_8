from django.http import HttpResponse
from django.shortcuts import render



def summary(request):
    return render(request, 'summary.html')

