import django_filters
from django_filters import UUIDFilter
from .models import Lieu, Evenement, imageLieu, imageEvenement


class ImageLieuFilter(django_filters.FilterSet):
    id = UUIDFilter(field_name='id__id', label='ID de l\'lieu')
    
class ImageEvenementFilter(django_filters.FilterSet):
    id = UUIDFilter(field_name='id__id', label='ID de l\'événement')