from django.db import models
from django.db import models
from filer.fields.image import FilerImageField


class Post(models.Model):
	title = models.CharField(max_length=300)
	feature_image = FilerImageField(related_name="post_image")