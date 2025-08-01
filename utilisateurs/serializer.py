from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Utilisateur, consulte, recherche, Note, Favoris
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer pour l'utilisateur
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'imageProfil', 'telephone', 'is_staff', 'is_active', 'password']
        read_only_fields = ['id']
        write_only_fields = ['password']
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = Utilisateur(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    # def update(self, instance, validated_data):
    #     image_profil = validated_data.pop('imageProfil', None)
    #     for attr, value in validated_data.items():
    #         setattr(instance, attr, value)
    #     if image_profil:
    #         instance.imageProfil = image_profil
    #     instance.save()
    #     return instance
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    
class ConsulteSerializer(serializers.HyperlinkedModelSerializer):
    utilisateur = serializers.HyperlinkedRelatedField(
        view_name='utilisateur-detail',
        read_only=True
    )
    lieu = serializers.HyperlinkedRelatedField(
        view_name='lieu-detail',
        read_only=True
    )
    evenement = serializers.HyperlinkedRelatedField(
        view_name='evenement-detail',
        read_only=True
    )
    
    class Meta: 
        model = consulte
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'date_consultation']
        
class RechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = recherche
        fields = ['id', 'utilisateur', 'mot_cle', 'date_creation']
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'note', 'commentaire', 'date_creation', 'date_modification']
    
