import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utilisateur(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    imageProfil = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    telephone = models.CharField(max_length=15, unique=True, null=True, blank=True)

    def __str__(self):
        return self.username
