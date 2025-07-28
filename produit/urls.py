from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LieuViewSet, EvenementViewSet, ImageLieuViewSet, ImageEvenementViewSet

# Création du routeur pour les vues des produits
router = DefaultRouter()
router.register(r'lieux', LieuViewSet, basename='lieu')
router.register(r'evenements', EvenementViewSet, basename='evenement')
router.register(r'image_lieux', ImageLieuViewSet, basename='image_lieu')
router.register(r'image_evenements', ImageEvenementViewSet, basename='image_evenement')

urlpatterns = [
    path('', include(router.urls)),
]