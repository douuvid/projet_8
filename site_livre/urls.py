from django.contrib import admin
from django.urls import include, path
from site_livre.views.logging import inscription
from site_livre.views.summary import summary
from site_livre.views.creer_ticket import creer_ticket
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView, PasswordChangeView, PasswordChangeDoneView

from authentification.views import book_list



urlpatterns = [
    # Admin
    path('admin/', admin.site.urls, name='admin'),

    # Pages principales
    path('', summary, name='home'),
    path('summary/', summary, name='summary'),
    path('inscription/', inscription, name='inscription'),
    path('create_ticket/', creer_ticket, name='create_ticket'),

    # Authentification
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Gestion des mots de passe
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),

    # Autres
    path('account/', include('allauth_2fa.urls')),
    path('books/', book_list, name='book_list'),
]

urlpatterns += staticfiles_urlpatterns()
