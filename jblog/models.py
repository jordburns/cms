from django.db import models
from filer.fields.image import FilerImageField
from djangocms_text_ckeditor.fields import HTMLField
from django.db import models
from cms.models.fields import PlaceholderField
from django.utils import timezone



class Category(models.Model):
	title = models.CharField(max_length=250)

class Post(models.Model):
	author = models.ForeignKey('auth.User')
	published = models.BooleanField(default=False)
	title = models.CharField(max_length=255)
	feature = FilerImageField(related_name="feature_image", help_text="This should be an image that represents the post")
	abstract = HTMLField(help_text="Text displayed on post list page")
	content = PlaceholderField('post_content')
	created = models.DateTimeField()
	published_date = models.DateTimeField(blank=True, null=True)
	slug = models.SlugField(max_length=40, unique=True, blank=True)


	def publish(self): 
		"""
		Publish or Un_publish Post.
		"""
		if self.published == True:
			self.published = False
			self.published_date = None
			self.save()
		else:
			self.published = True
			self.published_date = timezone.now()
			self.save()

	def get_absolute_url(self):
		return "/blog/post/%s/" % (self.slug)

	def __str__(self): 
		return self.title