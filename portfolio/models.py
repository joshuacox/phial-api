import os
import logging
from django.db import models, transaction
from django.dispatch import receiver

from django.core.files import File
from django_fine_uploader.signals import file_uploaded
#from fine_uploader.views import UploadView
from PIL import Image

logger = logging.getLogger('django')

class Category(models.Model):
    title       = models.CharField(max_length=200)
    abbv        = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    img_count   = models.IntegerField()
    hidden      = models.BooleanField()
    order       = models.IntegerField(default=0)

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


#@receiver(file_uploaded, sender=UploadView)
#def create_on_upload(sender, path, request, **kwargs):
#
#    photo_grp = Category.objects.filter(title__exact=request.POST.get('category'))[0]
#    img_model = Photo(category=photo_grp)
#
#    #TODO - come up with a better way to link image/thumb to model, this seems jenky
#    path = path.split("/")[-1]
#    #extract file name from path
#    img = os.path.splitext( path )
#    img_model.image = img[0] + img[1]
#    img_model.thumb = img[0] + '.thumbnail' + ".jpg"
#    img_model.save()
