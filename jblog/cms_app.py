from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _ 

class JBlogApp(CMSApp):
	name = _('JBlog App')
	urls = ['jblog.urls']


apphook_pool.register(JBlogApp)