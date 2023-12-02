from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Produit, Commande, CommentaireProduit
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'home.html')

@login_required
def profil(request):
    return render(request, 'profil.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})
def liste_produits(request):
    produits = Produit.objects.all()
    return render(request, 'liste_produits.html', {'produits': produits})

def detail_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    commentaires = CommentaireProduit.objects.filter(produit=produit)
    return render(request, 'detail_produit.html', {'produit': produit, 'commentaires': commentaires})

@login_required
def passer_commande(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)

    if request.method == 'POST':
        quantite = int(request.POST['quantite'])
        adresse_livraison = request.POST['adresse_livraison']

        # Vérifier si la quantité demandée est disponible
        if quantite <= produit.quantite_disponible:
            # Créer la commande
            commande = Commande(produit=produit, acheteur=request.user, quantite=quantite, adresse_livraison=adresse_livraison)
            commande.save()

            # Mettre à jour la quantité disponible du produit
            produit.quantite_disponible -= quantite
            produit.save()

            return render(request, 'commande_reussie.html', {'commande': commande})

        else:
            return render(request, 'quantite_indisponible.html', {'produit': produit})

    return render(request, 'passer_commande.html', {'produit': produit})

@login_required
def ajouter_commentaire(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)

    if request.method == 'POST':
        contenu = request.POST['contenu']
        commentaire = CommentaireProduit(produit=produit, auteur=request.user, contenu=contenu)
        commentaire.save()

        return HttpResponseRedirect('/produit/{}/'.format(produit_id))

    return render(request, 'ajouter_commentaire.html', {'produit': produit})
