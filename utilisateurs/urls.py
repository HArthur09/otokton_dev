from utilisateurs.views import UtilisateurViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Création du routeur pour les vues de l'utilisateur
router = DefaultRouter()

router.register(r'utilisateurs', UtilisateurViewSet, basename='utilisateur')

urlpatterns = [
    path('', include(router.urls)),
]