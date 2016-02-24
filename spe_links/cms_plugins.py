from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import SpeLinkPluginModel, SpeLinkCategory, SpeLink
from django.utils.translation import ugettext as _


class SpeLinkPluginPublisher(CMSPluginBase):
    model = SpeLinkPluginModel  # model where plugin data are saved
    module = _("Links")
    name = _("Link Plugin")  # name of the plugin in the interface
    render_template = "spe_links/links_plugin.html"
    cache = False

    def render(self, context, instance, placeholder):
        if instance and instance.category and instance.category.id:

            if (instance.category.code == 'SPENEWS'):
                instance.links = SpeLink.objects.filter(category_id__exact=instance.category.id).values().order_by("-pub_date")
            else:
                instance.links = SpeLink.objects.filter(category_id__exact=instance.category.id).values().order_by("title")
#            instance.category = SpeLinkCategory.objects.get(pk=instance.catkey)


        context.update({'instance': instance})

        return context

plugin_pool.register_plugin(SpeLinkPluginPublisher)  # register the plugin