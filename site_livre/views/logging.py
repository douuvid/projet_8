from django.http import HttpResponse
from django.shortcuts import render



def ca_c_la_vue(request):
    return render(request, 'logging_template.html')


