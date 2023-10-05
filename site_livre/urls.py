from django.contrib import admin
from django.urls import include, path
from .views.logging import inscription
from .views.summary import summary
from .views.creer_ticket import creer_ticket
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetView, 
                                       PasswordResetDoneView, PasswordResetConfirmView, 
                                       PasswordResetCompleteView, PasswordChangeView, 
                                       PasswordChangeDoneView)
from authentification.views import book_list
from authentification.views import home


from django.urls import path
#from . import views


urlpatterns = [
    # Admin
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    #path('logging_template/', votre_vue, name='inscription'),
    path('inscription/', inscription, name='inscription'),



    # Pages principales
   # path('', LoginView.as_view(template_name='registration/logging_template.html'), name='home'),
    #path('summary/', summary, name='summary'),
    
    #path('creer-ticket/', creer_ticket, name='creer_ticket'),

    # Authentification
   
    

    # # Gestion des mots de passe
    # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # # Autres
    # path('account/', include('allauth_2fa.urls')),
    # path('books/', book_list, name='book_list'),
    # path('auth/', include('authentification.urls')),
    
    

    # Supprimez cette ligne car il n'y a pas de module 'site_livre.urls'
    # path('', include('site_livre.urls', namespace='site_livre')),
]

urlpatterns += staticfiles_urlpatterns()
