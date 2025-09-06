from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework.decorators import action
from rest_framework import viewsets, status
from .models import Utilisateur, consulte, recherche, Note, Favoris
from .serializer import UtilisateurSerializer, LoginSerializer, ConsulteSerializer, ConsulteReadSerializer, RechercheSerializer, NoteSerializer, FavorisSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions


# Create your views here.
class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer
    lookup_field = 'id'
    
    @action(detail=False, methods=['post'], url_path='login', permission_classes=[permissions.AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            
            user_data = UtilisateurSerializer(user, context={"request": request}).data
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'user': user_data
            })
        return Response({'detail': 'Identifiants invalides.'}, status=status.HTTP_401_UNAUTHORIZED)

class ConsulteViewSet(viewsets.ModelViewSet):
    queryset = consulte.objects.all()
    lookup_field = 'id'
    
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ConsulteReadSerializer
        return ConsulteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['utilisateur', 'lieu', 'evenement', 'date_consultation']
    
class RechercheViewSet(viewsets.ModelViewSet):
    queryset = recherche.objects.all()
    serializer_class = RechercheSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['utilisateur', 'mot_cle', 'date_creation']

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['utilisateur', 'lieu', 'evenement', 'note', 'date_creation', 'date_modification']
    
class FavorisViewSet(viewsets.ModelViewSet):
    queryset = Favoris.objects.all()
    serializer_class = FavorisSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['utilisateur', 'lieu', 'evenement', 'date_ajout']
    


        
