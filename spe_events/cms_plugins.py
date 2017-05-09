import requests
import json
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.utils.translation import ugettext_lazy as _

from django.contrib.gis.geoip import GeoIP

from .models import EventsByCurrentIPPlugin, ImageItems, ImageItemsPlugin
from .settings import EVENT_PERSONALIZATION_SERVER
from mainsite.common import get_context_variable


class ShowEventsByCurrentLocationPluginPlugin(CMSPluginBase):
    model = EventsByCurrentIPPlugin
    allow_children = False
    cache = False
    module = _('Events')
    name = _('Events near user')
    text_enabled = False
    render_template = 'spe_events/plugins/location.html'

    def render(self, context, instance, placeholder):
        request = context['request']
        WS_EVENTS_URL = get_context_variable(request, "WS_EVENTS_URL",
                                             "http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3")
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


class ImageItemPluginInstance(CMSPluginBase):
    model = ImageItemsPlugin
    name = "Image Items"
    render_template = "spe_events/plugins/image_items/ii_boxes.html"
    allow_children = True
    module = 'Events'

    def render(self, context, instance, placeholder):
        image_items = ImageItems.objects.filter(item_list=instance.item_list)
        # previous_is_child = 0
        # for item in reversed(image_items):
        #     item.is_dropdown_node = previous_is_child
        #     if item.level == 2 or item.level == 3:
        #         previous_is_child = 1
        #         item.is_dropdown_node = 0
        #     else:
        #         previous_is_child = 0
        # previous_is_child = 0
        # for item in image_items:
        #     if item.level == 3:
        #         item.is_dropdown_header = True
        #     if item.level == 4:
        #         item.is_divider = True
        #     if previous_is_child and item.level == 1:
        #         item.is_back_up = 1
        #     else:
        #         item.is_back_up = 0
        #     if item.level == 2 or item.level == 3:
        #         previous_is_child = 1
        #     else:
        #         previous_is_child = 0
        context.update({
            'event_id': instance.item_list.event_id,
            'items': image_items,
        })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(ShowEventsByCurrentLocationPluginPlugin)
plugin_pool.register_plugin(ImageItemPluginInstance)
