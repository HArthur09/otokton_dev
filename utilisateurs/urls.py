from utilisateurs.views import UtilisateurViewSet, ConsulteViewSet, RechercheViewSet, NoteViewSet, FavorisViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Création du routeur pour les vues de l'utilisateur
router = DefaultRouter()

router.register(r'utilisateurs', UtilisateurViewSet, basename='utilisateur')
router.register(r'consulte', ConsulteViewSet, basename='consulte')
router.register(r'recherches', RechercheViewSet, basename='recherche')
router.register(r'notes', NoteViewSet, basename='note')
router.register(r'favoris', FavorisViewSet, basename='favoris')



urlpatterns = [
    path('', include(router.urls)),
]