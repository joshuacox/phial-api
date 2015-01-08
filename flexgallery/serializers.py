from django.forms import widgets
from rest_framework import serializers, pagination
from django.core.paginator import Paginator
from portfolio.models import Category, Photo


class CategorySerializer(serializers.ModelSerializer):
    photos = serializers.RelatedField(many=True)

    class Meta:
        model = Category
        fields = ('title', 'urlified', 'abbv', 'description', 'hidden', 'img_count', 'id')


class PhotoSerializer(serializers.ModelSerializer):
    category_image = serializers.Field()

    class Meta:
        model = Photo
        category = serializers.Field(source='category.title')
        fields = ('pub_date', 'image', 'thumb', 'description', 'id', 'category', 'category_image')

class PaginatedPhotoSerializer(pagination.PaginationSerializer):
    """
    Serializes page objects of photo querysets.
    """
    class Meta:
        object_serializer_class = PhotoSerializer