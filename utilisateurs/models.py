import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from produit.models import Lieu, Evenement

# Create your models here.
class Utilisateur(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imageProfil = models.ImageField(upload_to='images/profile_images/', null=True, blank=True)
    telephone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
    
class consulte(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='consultes')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='consultes', null=True, blank=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='consultes', null=True, blank=True)
    date_consultation = models.DateTimeField(auto_now_add=True) 
    
class recherche(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='recherches')
    mot_cle = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Recherche de {self.utilisateur.username} pour '{self.mot_cle}'"

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='notes')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='notes', null=True, blank=True)
    note = models.IntegerField()
    commentaire = models.TextField(null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note by {self.utilisateur.username} for {self.lieu.nom if self.lieu else self.evenement.titre.nom}"
    
    
class Favoris(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='favoris')
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='favoris', null=True, blank=True)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='favoris', null=True, blank=True)
    date_ajout = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Favori by {self.utilisateur.username} for {self.lieu.nom if self.lieu else self.evenement.titre.nom}"
