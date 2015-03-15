from django.views import generic
from django.shortcuts import redirect
from django.http import Http404
from .models import Post, Category
from django.shortcuts import render


class IndexView(generic.ListView):
    template_name = 'jblog/post_list.html'
    context_object_name = 'latest_post_list'
    paginate_by = 4

    def get_queryset(self):
    	if self.request.user.has_perm('jblog.add_post'):
    		return Post.objects.all().order_by('published', '-published_date', '-created')
    	else:
        	return Post.objects.filter(published=True).order_by('-published_date')

    def get_context_data(self, *args, **kwargs):
    	context = super(IndexView, self).get_context_data(*args, **kwargs)
    	context['post_categories'] = Category.objects.all()
    	return context 


class DetailView(generic.DetailView):
    model = Post
    template_name = 'jblog/detail.html'

    def get_object(self, queryset=None):
    	obj = super(DetailView, self).get_object()
    	if obj.published or self.request.user.has_perm('jblog.change_post'):
    		return obj

    	else:
    		raise Http404("Incorrect Permissions!")



def publish_post(request, slug):
	if request.user.has_perm('jblog.change_post'):
		post = Post.objects.get(slug=slug)
		post.publish()
		return redirect('jblog:index')
	else:
		raise Http404("Incorrect Permissions!")
