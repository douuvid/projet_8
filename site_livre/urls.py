"""site_livre URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from site_livre.views.logging import inscription
from site_livre.views.not_found import page_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from site_livre.views.summary import summary
from site_livre.views.creer_ticket import creer_ticket

urlpatterns = [
    # première page, pas de connexion 
    path('summary/', summary),# 1/10s
    path('inscription/', inscription),# 2/10
    path('admin/', admin.site.urls),
    path('cree_un_ticket/', creer_ticket),
    path('', page_404),
    
    
]

urlpatterns += staticfiles_urlpatterns()
