from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic

from .models import Post


class IndexView(generic.ListView):
    template_name = 'jblog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        return Post.objects.all()[:5]


class DetailView(generic.DetailView):
    model = Post
    template_name = 'jblog/detail.html'