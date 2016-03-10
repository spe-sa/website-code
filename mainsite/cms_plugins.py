from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
# from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import AdSpeedZonePlugin
from .models import TitleBarPlugin
from .models import TextPlugin


class ShowAdSpeedZonePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Advertising')
    render_template = 'plugins/adspeed_zone_plugin.html'
    text_enabled = False
    model = AdSpeedZonePlugin
    name = _("AdSpeed Ad")

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

class ShowTitlePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Components')
    render_template = 'plugins/title_plugin.html'
    text_enabled = False
    model = TitleBarPlugin
    name = _("Title Bar")

    def render(self, context, instance, placeholder):
        context.update({'title': instance.title})
        return context

class ShowTextPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Components')
    render_template = 'plugins/text_plugin.html'
    text_enabled = False
    model = TextPlugin
    name = _("Text")

    def render(self, context, instance, placeholder):
        context.update({'text': instance.text})
        return context

plugin_pool.register_plugin(ShowAdSpeedZonePlugin)
plugin_pool.register_plugin(ShowTitlePlugin)
plugin_pool.register_plugin(ShowTextPlugin)
