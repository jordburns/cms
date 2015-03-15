# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djangocms_text_ckeditor.fields
import cms.models.fields
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0003_auto_20140926_2347'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255)),
                ('abstract', djangocms_text_ckeditor.fields.HTMLField(help_text=b'Text displayed on post list page')),
                ('created', models.DateTimeField()),
                ('published_date', models.DateTimeField(null=True, blank=True)),
                ('slug', models.SlugField(unique=True, max_length=40, blank=True)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'post_content', editable=False, to='cms.Placeholder', null=True)),
                ('feature', filer.fields.image.FilerImageField(related_name='feature_image', to='filer.Image', help_text=b'This should be an image that represents the post')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
