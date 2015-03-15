from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from cms.toolbar_pool import toolbar_pool
from cms.toolbar_base import CMSToolbar


@toolbar_pool.register
class PollToolbar(CMSToolbar):
    def populate(self):
        if self.is_current_app:
            menu = self.toolbar.get_or_create_menu('jblog-app', _('JBlog'))
            uadd = reverse('admin:jblog_post_add')
            ulist = reverse('admin:jblog_post_changelist')
            menu.add_modal_item(_('Add Post'), url=uadd)
            menu.add_modal_item(_('Post List'), url=ulist)