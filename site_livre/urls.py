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
from site_livre.views.logging import ca_c_la_vue
from site_livre.views.not_found import page_404
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from site_livre.views.summary import summary

urlpatterns = [
    # première page, pas de connexion 
    path('inscription/', ca_c_la_vue),
    path('admin/', admin.site.urls),
    path('', page_404),
    path('sommaire/', summary),
    
]

urlpatterns += staticfiles_urlpatterns()
