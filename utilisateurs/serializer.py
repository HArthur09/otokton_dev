from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Utilisateur, consulte, recherche, Note, Favoris
from produit.models import Lieu, Evenement
from produit.serializer import LieuSerializer, EvenementSerializer  
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# Serializer pour l'utilisateur
class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = ['id', 'first_name', 'last_name', 'username', 'email', 'imageProfil', 'telephone', 'is_staff', 'is_active', 'password']
        read_only_fields = ['id']
        write_only_fields = ['password']
        extra_kwargs = {
            'password': {'write_only': True}
        }
       
        def validate_image(self, value):
            if value:
                valid_extensions = ['jpg', 'jpeg', 'png']
                ext = os.path.splitext(value.name)[1].lower()
                if ext not in valid_extensions:
                    raise serializers.ValidationError("Extension non supporté. Les formats supportés sont:" + (valid_extensions))
                
                max_size = 5 * 1024 * 1024  # 5 MB
                if value.size > max_size:
                    raise serializers.ValidationError("La taille de l'image ne doit pas dépasser 5 Mo.")
            return value
     
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
        queryset = Utilisateur.objects.all(),
        lookup_field = 'id'
    )
    lieu = serializers.HyperlinkedRelatedField(
        view_name='lieu-detail',
        queryset = Lieu.objects.all(),
        lookup_field = 'id'
    )
    evenement = serializers.HyperlinkedRelatedField(
        view_name='evenement-detail',
        queryset = Evenement.objects.all(),
        lookup_field = 'id'
    )
    
    class Meta: 
        model = consulte
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'date_consultation']
        extra_kwargs = {
            'url' : {'view_name': 'consulte-detail', 'lookup_field' : 'id'}
        }
        
class ConsulteReadSerializer(serializers.HyperlinkedModelSerializer):
    utilisateur = UtilisateurSerializer()
    lieu = LieuSerializer()
    evenement = EvenementSerializer()
    
    class Meta: 
        model = consulte
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'date_consultation']
        extra_kwargs = {
            'url' : {'view_name': 'consulte-detail', 'lookup_field' : 'id'}
        }
        
class RechercheSerializer(serializers.ModelSerializer):
    class Meta:
        model = recherche
        fields = ['id', 'utilisateur', 'mot_cle', 'date_creation']
        
class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'note', 'commentaire', 'date_creation', 'date_modification']
        
class FavorisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favoris
        fields = ['id', 'utilisateur', 'lieu', 'evenement', 'date_ajout']
    
