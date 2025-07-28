from django.db import models
import uuid

# Create your models here.
class Lieu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nom = models.CharField(max_length=255)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    text_descriptif = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/lieux/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    est_actif = models.BooleanField(default=True)
    
    def __str__(self):
        return self.nom if self.nom else "Lieu sans nom"
    
class Evenement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    titre = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='evenements')
    description_lieu = models.TextField()
    latitude = models.FloatField()
    longtitude = models.FloatField()
    heure = models.TimeField(null=True, blank=True)
    contact = models.CharField(max_length=30)
    texte_description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/evenements/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    en_cours = models.BooleanField(default=True)
    
    def __str__(self):
        return self.titre.nom if self.titre else "Événement sans titre"
    
class imageLieu(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    lieu = models.ForeignKey(Lieu, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/lieux/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Image for {self.lieu.nom}" if self.lieu else "Image without a place"
    
class imageEvenement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='images/evenements/', null=True, blank=True)
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Image for {self.evenement.titre.nom}" if self.evenement else "Image without an event"
    
    