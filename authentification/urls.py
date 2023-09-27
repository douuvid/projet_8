from django.urls import include, path
from .views import book_list
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
   

    # Pages principales
    #path('', book_list, name='home'),
    
]

urlpatterns += staticfiles_urlpatterns()
