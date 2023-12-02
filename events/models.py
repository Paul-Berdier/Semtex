# models.py
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # Vos autres champs ici
    email = models.EmailField(unique=True)
    # Modifiez ces lignes
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name='customuser_set',  # Ajoutez cette ligne
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name='customuser_set',  # Ajoutez cette ligne
    )
class Boutique(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    proprietaire = models.ForeignKey(User, on_delete=models.CASCADE)

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite_disponible = models.IntegerField()
    boutique = models.ForeignKey(Boutique, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)

class Commande(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    acheteur = models.ForeignKey(User, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    adresse_livraison = models.TextField()
    date_commande = models.DateTimeField(auto_now_add=True)

class CommentaireProduit(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    auteur = models.ForeignKey(User, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

# Ajoutez d'autres modèles selon les besoins, tels que le suivi des ventes, des remises, etc.
