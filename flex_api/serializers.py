from django.forms import widgets
from rest_framework import serializers, pagination
from django.core.paginator import Paginator
from flex_api.models import Category, Photo


class CategorySerializer(serializers.ModelSerializer):
    photos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="photo-detail")

    class Meta:
        model = Category
        fields = ('title', 'abbv', 'description', 'img_count', 'id', 'photos')


class PhotoSerializer(serializers.ModelSerializer):
    category_image = serializers.ReadOnlyField()

    class Meta:
        model = Photo
        category = serializers.Field(source='category.title')
        fields = ('pub_date', 'image', 'id', 'category', 'category_image')
