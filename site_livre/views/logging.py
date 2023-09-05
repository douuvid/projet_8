from django.http import HttpResponse
from django.shortcuts import render



def inscription(request):
    return render(request, 'logging_template.html')




