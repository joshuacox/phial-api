from django.forms import widgets
from rest_framework import serializers, pagination
from django.core.paginator import Paginator
from flex_api.models import Category, Photo
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    owner  = serializers.ReadOnlyField(source='owner.username')
    photos = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="photo-detail")

    class Meta:
        model = Category
        fields = ('title', 'abbv', 'description', 'img_count', 'id', 'owner', 'photos',)

class PhotoSerializer(serializers.ModelSerializer):
    #category_image = serializers.ReadOnlyField()
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    image    = serializers.ImageField()

    class Meta:
        model = Photo
        fields = (
		'pub_date',
		'image',
		'id',
		'category',
		#'category_image',
	)

class UserSerializer(serializers.ModelSerializer):
    categories = serializers.PrimaryKeyRelatedField(many=True, queryset=Category.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'categories', )
