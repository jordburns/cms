from django.contrib import admin
from .models import Post, Category
from django.utils import timezone
from django.utils.text import slugify


class PostAdmin(admin.ModelAdmin):
	fields = ('title', 'feature', 'abstract')
	list_display = ('title', 'published', 'created', 'published_date', 'author')
	search_fields = ('title',)
	ordering = ('published', '-published_date', '-created')
	date_hierarchy = 'created'

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		obj.created = timezone.now()
		obj.slug = slugify(unicode(obj.title))
		obj.save()

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Category)