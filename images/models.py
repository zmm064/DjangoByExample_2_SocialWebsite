from django.db import models
from django.conf import settings
from django.utils.text import slugify
# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_created')
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)

    title       = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=200, blank=True)
    url         = models.URLField()
    image       = models.ImageField(upload_to='images/%Y/%m/%d')
    description = models.TextField(blank=True)
    created     = models.DateTimeField(auto_now_add=True, db_index=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        '''重写save方法，为图片自动生成slug'''
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)