from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
# from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import AdSpeedZonePlugin


class ShowAdSpeedZonePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Advertising')
    render_template = 'adspeed_zone_plugin.html'
    text_enabled = False
    model = AdSpeedZonePlugin
    name = _("AdSpeed Ad")

    def render(self, context, instance, placeholder):
        context.update({'div_id': instance.div_id})
        context.update({'div_class': instance.div_class})
        context.update({'zid': instance.zid})
        context.update({'aid': instance.aid})
        return context


plugin_pool.register_plugin(ShowAdSpeedZonePlugin)
