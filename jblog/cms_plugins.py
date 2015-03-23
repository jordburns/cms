from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext as _ 
from .models import Post
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


class LatestPostPlugin(CMSPluginBase):
    module = _('jblog')
    name = _('LatestPost')
    model = CMSPlugin
    render_template = 'jblog/latest_post.html'

    def render(self, context, instance, placeholder):
        try:
            context['latest_post'] = Post.objects.filter(published=True).latest(field_name='published_date')
            return context
        except ObjectDoesNotExist:
            context['latest_post'] = None
            return context


plugin_pool.register_plugin(LatestPostPlugin)