from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.geoip import GeoIP

from .models import EventsByCurrentIPPlugin

class ShowEventsByCurrentLocationPluginPlugin(CMSPluginBase):
    model = EventsByCurrentIPPlugin
    allow_children = False
    cache = False
    module = _('Events')
    name = _('Events near user')
    text_enabled = False
    render_template = 'spe_events/plugins/location.html'
    #render_plugin = False

    def render(self, context, instance, placeholder):
        g = GeoIP()
        ip = context['request'].META.get('REMOTE_ADDR', None) 
        ip = '192.152.183.2'
        if ip:
            loc = g.city(ip)
            req_str = 'http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3?latitude=' + str(loc['latitude']) + '&longitude=' + str(loc['longitude']) + "&num=" + str(instance.number) + "&numKm=" + str(instance.radius)
            req_str = req_str + "&discipline="
            for discipline in instance.disciplines.all():
                req_str = req_str + discipline.eva_code
            req_str = req_str + "&eventtype="
            for type in instance.types.all():
                req_str = req_str + type.name + ','
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            try:
                r = requests.get(req_str, headers=headers)
                context.update({'meetings': r.json()})
            except:
                pass
        else:
            loc = None
        context.update({'location': loc})
        return context

plugin_pool.register_plugin(ShowEventsByCurrentLocationPluginPlugin)
