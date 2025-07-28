from rest_framework import serializers
from .models import Lieu, Evenement, imageLieu, imageEvenement


class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = [
            'id', 'nom', 'description', 'latitude', 'longitude',
            'text_descriptif', 'image', 'date_creation', 'date_modification', 'est_actif'
        ]
        
class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = [
            'id', 'titre', 'description_lieu', 'latitude', 'longtitude',
            'heure', 'contact', 'texte_description', 'image',
            'date_creation', 'date_modification', 'en_cours'
        ]

class ImageLieuSerializer(serializers.HyperlinkedModelSerializer):
    lieu = serializers.HyperlinkedRelatedField(
        view_name='lieu-detail',
        read_only=True
    )
    
    class Meta:
        model = imageLieu
        fields = ['url', 'id', 'lieu', 'image', 'date_creation', 'date_modification']
        
class ImageLieuReadSerializer(serializers.HyperlinkedModelSerializer):
    lieu = LieuSerializer()
    lookup_field = 'id'
    
    class Meta:
        model = imageLieu
        fields = ['url', 'id', 'lieu', 'image', 'date_creation', 'date_modification']
        extra_kwargs = {
            'url': {'view_name': 'imageLieu-detail', 'lookup_field': 'id'}
        }
        
        
class ImageEvenementSerializer(serializers.HyperlinkedModelSerializer):
    evenement = serializers.HyperlinkedRelatedField(
        view_name='evenement-detail',
        read_only=True
    )
    
    class Meta:
        model = imageEvenement
        fields = ['url', 'id', 'evenement', 'image', 'date_creation', 'date_modification']
        
class ImageEvenementReadSerializer(serializers.HyperlinkedModelSerializer):
    evenement = EvenementSerializer()
    lookup_field = 'id'
    
    class Meta:
        model = imageEvenement
        fields = ['url', 'id', 'evenement', 'image', 'date_creation', 'date_modification']
        extra_kwargs = {
            'url': {'view_name': 'imageEvenement-detail', 'lookup_field': 'id'}
        }
        
        