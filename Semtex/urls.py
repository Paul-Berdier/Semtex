"""
URL configuration for Semtex project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import include,path
from events import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('liste-produits/', views.liste_produits, name='liste_produits'),
    path('detail-produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('profil/', views.profil, name='profil'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
    path('produit/<int:produit_id>/', views.detail_produit, name='detail_produit'),
    path('produit/<int:produit_id>/commande/', views.passer_commande, name='passer_commande'),
    path('produit/<int:produit_id>/commentaire/', views.ajouter_commentaire, name='ajouter_commentaire'),
    path('accounts/', include('allauth.urls')),
    # Ajoutez d'autres routes au besoin
]

