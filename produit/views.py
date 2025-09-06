from django.shortcuts import render
from utilisateurs.models import Utilisateur
from .serializer import LieuSerializer, EvenementSerializer, ImageLieuSerializer, ImageEvenementSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from .models import Lieu, Evenement, imageLieu, imageEvenement


# Create your views here.
class LieuViewSet(viewsets.ModelViewSet):
    queryset = Lieu.objects.all()
    serializer_class = LieuSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['est_actif', 'date_creation']
    #permission_classes = [IsAuthenticated]
    lookup_field = 'id'
    
    def create(self, request, *args, **kwargs):
        #On surcharge la méthode create pour mieux gérer les réponses
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        header = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=header)
    
    def update(self, request, *args, **kwargs):
        #On surcharge la méthode update pour mieux gérer les images
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
class EvenementViewSet(viewsets.ModelViewSet):
    queryset = Evenement.objects.all()
    serializer_class = EvenementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['en_cours', 'date_creation', 'date_modification']
    lookup_field = 'id'
    
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
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['evenement', 'date_creation', 'date_modification']
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ImageEvenementReadSerializer
        return ImageEvenementSerializer


