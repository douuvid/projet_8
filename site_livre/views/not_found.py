from django.http import HttpResponse

def page_404(request):
    return HttpResponse("Cette page n'existe pas ", status = 404)