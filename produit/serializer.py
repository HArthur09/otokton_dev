from rest_framework import serializers
from .models import Lieu, Evenement, imageLieu, imageEvenement


class LieuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lieu
        fields = [
            'id', 'nom', 'description', 'latitude', 'longitude',
            'text_descriptif', 'image', 'date_creation', 'date_modification', 'est_actif'
        ]
        read_only_fields = ['id', 'date_creation', 'date_modification']
        
        def validate_image(self, value):
            if value:
                valid_extensions = ['jpg', 'jpeg', 'png', ".gif", ".webp"]
                ext = os.path.splitext(value.name)[1].lower()
                if ext not in valid_extensions:
                    raise serializers.ValidationError("Extension non supporté. Les formats supportés sont:" + (valid_extensions))
                
                maws_size = 5 * 1024 * 1024  # 5 MB
                if value.size > max_size:
                    raise serializers.ValidationError("La taille de l'image ne doit pas dépasser 5 Mo.")
            return value
        
class EvenementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evenement
        fields = [
            'id', 'titre', 'latitude', 'longtitude',
            'heure', 'contact', 'texte_description', 'image',
            'date_creation', 'date_modification', 'en_cours'
        ]
        read_only_fields = ['id', 'date_creation', 'date_modification']
        
        def validate_image(self, value):
            if value:
                valid_extensions = ['jpg', 'jpeg', 'png', ".gif", ".webp"]
                ext = os.path.splitext(value.name)[1].lower()
                if ext not in valid_extensions:
                    raise serializers.ValidationError("Extension non supporté. Les formats supportés sont:" + (valid_extensions))
                
                max_size = 5 * 1024 * 1024  # 5 MB
                if value.size > max_size:
                    raise serializers.ValidationError("La taille de l'image ne doit pas dépasser 5 Mo.")
            return value

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
        
        