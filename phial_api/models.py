import os
import logging
from django.db import models, transaction
from django.dispatch import receiver

from django.core.files import File
from PIL import Image

logger = logging.getLogger('django')

class Category(models.Model):
    title       = models.CharField(max_length=200)
    abbv        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    img_count   = models.IntegerField()
    hidden      = models.BooleanField(default=False)
    order       = models.IntegerField(default=0)
    owner       = models.ForeignKey('auth.User', related_name="categories")

    @transaction.atomic
    def next_sku(self):
        """
        Get the next sku for this category - called on photo.create
        """
        self.img_count += 1
        self.save()
        return self.img_count

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order',)

class Photo(models.Model):
    category    = models.ForeignKey(Category, related_name="photos")
    description = models.TextField(blank=True)
    pub_date    = models.DateTimeField(auto_now_add=True, blank=True)
    image       = models.ImageField(max_length=100, blank=True)
    thumb       = models.ImageField(max_length=100, blank=True)

    category_auto_key = models.IntegerField()

    def category_image(self):
        return self.category.abbv+"-"+str(self.category_auto_key)

    def pre_save(self, obj):
        """
        pre_save the Category reference
        """
        obj.category = self.request.category

    def save(self, *args, **kwargs):
        """
        Overwrite save to increment the category counter save it,
        and set the label of the photo
        """
        if not self.category_auto_key:
            self.category_auto_key = self.category.next_sku()

        # call the super class' save method
        super(Photo, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.category.abbv +"-"+ str(self.category_auto_key)

    class Meta:
        ordering = ('pub_date',)
