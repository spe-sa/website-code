import requests
import json
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.geoip import GeoIP

from .models import EventsByCurrentIPPlugin # , EventMenuPluginModel, EventMenuModel
from .settings import EVENT_PERSONALIZATION_SERVER
from mainsite.common import get_context_variable

# class EventMenuPlugin(CMSPluginBase):
#     model = EventMenuPluginModel
#     allow_children = False
#     cache = False
#     module = _('Events')
#     name = _('Event Menu')
#     text_enabled = False
#     render_template = 'spe_events/plugins/event_menu.html'
#
#     def render(self, context, instance, placeholder):
#         # get the menu for this meeting code if there is any
#         if instance.event_code:
#             menus = EventMenuModel.objects.filter(event_code=instance.event_code).all()
#         else:
#             menus=None
#         context.update({'event_code': instance.event_code,
#                        'menu_items': menus})
#         return context

class ShowEventsByCurrentLocationPluginPlugin(CMSPluginBase):
    model = EventsByCurrentIPPlugin
    allow_children = False
    cache = False
    module = _('Events')
    name = _('Events near user')
    text_enabled = False
    render_template = 'spe_events/plugins/location.html'

    # render_plugin = False

    def render(self, context, instance, placeholder):
        request = context['request']
        WS_EVENTS_URL = get_context_variable(request, "WS_EVENTS_URL", "http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3")
        g = GeoIP()
        # ip = context['request'].META.get('REMOTE_ADDR', None)
        ip = context['request'].META.get('HTTP_X_REAL_IP', None)
        if not ip:
            ip = '192.152.183.80'
        if ip:
            loc = g.city(ip)
            if loc:
                req_str = WS_EVENTS_URL
                req_str += '?latitude=' + str(loc['latitude']) + '&longitude=' + str(loc['longitude'])
                req_str += '&num=' + str(instance.number) + '&numKm=' + str(instance.radius)
                req_str += '&discipline='
                for discipline in instance.disciplines.all():
                    req_str = req_str + discipline.eva_code + ':'
                req_str += '&eventtype='
                for type in instance.types.all():
                    req_str = req_str + type.name + ','
                headers = {'Accept': 'application/json'}
                try:
                    r = requests.get(req_str, headers=headers)
                    context.update({'events': r.json()})
                except:
                    pass
        else:
            loc = None
        context.update({'location': loc})
        return context


plugin_pool.register_plugin(ShowEventsByCurrentLocationPluginPlugin)
# plugin_pool.register_plugin(EventMenuPlugin)
