from django.shortcuts import render
from utilisateurs.models import Utilisateur
from .serializer import LieuSerializer, EvenementSerializer, ImageLieuSerializer, ImageEvenementSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Lieu, Evenement, imageLieu, imageEvenement


# Create your views here.
class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['est_actif', 'date_creation']
    
class EvenementViewSet(viewsets.ModelViewSet):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['en_cours', 'date_creation', 'date_modification']
    
class ImageLieuViewSet(viewsets.ModelViewSet):
    queryset = imageLieu.objects.select_related('id')
    serializer_class = ImageLieuSerializer
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ImageLieuReadSerializer
        return ImageLieuSerializer
    
class ImageEvenementViewSet(viewsets.ModelViewSet):
    queryset = imageEvenement.objects.select_related('id')
    serializer_class = ImageEvenementSerializer
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ImageEvenementReadSerializer
        return ImageEvenementSerializer


