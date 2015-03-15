from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^post/(?P<slug>[-_\w]+)/$', views.DetailView.as_view(), name='post-detail'),
	url(r'^publish_post/(?P<slug>[-_\w]+)/$', views.publish_post, name='publish-post'),
)