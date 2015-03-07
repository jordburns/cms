from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField

class Post(models.Model):
    title = models.CharField(max_length=255)
    feature = FilerImageField(related_name="feature_image")
    abstract = HTMLField(blank=True, null=True)