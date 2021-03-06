from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import SpeLinkPluginModel, SpeLink, PageLinkSetPlugin, PageLink
from django.utils.translation import ugettext as _



class SpeLinkPluginPublisher(CMSPluginBase):
    model = SpeLinkPluginModel  # model where plugin data are saved
    module = _("Links")
    name = _("Links Plugin")  # name of the plugin in the interface
    render_template = "spe_links/plugins/links_plugin.html"
    cache = True

    def render(self, context, instance, placeholder):
        if instance.category and instance.category.id:
            instance.links = SpeLink.objects.filter(category_id__exact=instance.category.id).order_by("title")

        context.update({'instance': instance})

        return context

class PageLinkSetPluginInstance(CMSPluginBase):
    model = PageLinkSetPlugin
    name = "SPE Set of Links"
    render_template = "spe_links/plugins/bootstrap_links.html"
    allow_children = True
    module = 'Links'

    def render(self, context, instance, placeholder):
        links = PageLink.objects.filter(page_set=instance.link_set)
        context.update({
            'instance': instance,
            'links': links
        })
        return context


plugin_pool.register_plugin(PageLinkSetPluginInstance)
plugin_pool.register_plugin(SpeLinkPluginPublisher)  # register the plugin
