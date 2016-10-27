import datetime
# from cms.models import CMSPlugin
import math
import requests
import json

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from django.contrib.gis.geoip import GeoIP
from mainsite.context_processors import spe_context

from .models import Promotion, PromotionListingPlugin
from .models import SimpleEventPromotion, SimpleEventPromotionListingPlugin
from .models import EventPromotionNearLocationListingPlugin, EventPromotionNearUserListingPlugin, EventPromotionByDisciplineListingPlugin

class ShowPromotionListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True
    allow_children = False
    cache = False
    module = ('Advertising')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = SimpleEventPromotionListingPlugin
    name = ("Promotion Listing")

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        
        if instance.disciplines.all():
            objects = objects.filter(disciplines__in=instance.disciplines.all())

        request = context['request']
        g = GeoIP()
        # ip = context['request'].META.get('REMOTE_ADDR', None)
        ip = context['request'].META.get('HTTP_X_REAL_IP', None)
        if not ip:
            ip = '192.152.183.80'
        if ip:
            loc = g.city(ip)
            if loc:
                latitude = loc['latitude']
                longitude = loc['longitude']

        new_objects = []

        for x in objects:
            dlat = math.radians(x.latitude - latitude)
            dlon = math.radians(x.longitude - longitude)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
                * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = 6371 * c
           
            if d <= instance.radius:
                new_objects.append(x)

        objects = new_objects[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()
        
        context.update({'promos': objects})
        self.render_template = instance.template
        return context

class ShowEventNearLocationPromotionListing(CMSPluginBase):
    class Meta:
        abstract = True
    allow_children = False
    cache = False
    module = ('Advertising')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionNearLocationListingPlugin
    name = ("Events Near Location Promotion Listing")

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        
        new_objects = []

        for x in objects:
            dlat = math.radians(x.latitude - instance.latitude)
            dlon = math.radians(x.longitude - instance.longitude)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(instance.latitude)) \
                * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = 6371 * c
           
            if d <= instance.radius:
                new_objects.append(x)

        objects = new_objects[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()
        
        context.update({'promos': objects})
        self.render_template = instance.template
        return context

class ShowEventNearUserPromotionListing(CMSPluginBase):
    class Meta:
        abstract = True
    allow_children = False
    cache = False
    module = ('Advertising')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionNearUserListingPlugin
    name = ("Events Near User Promotion Listing")

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        
        request = context['request']
        g = GeoIP()
        # ip = context['request'].META.get('REMOTE_ADDR', None)
        ip = context['request'].META.get('HTTP_X_REAL_IP', None)
        if not ip:
            ip = '192.152.183.80'
        if ip:
            loc = g.city(ip)
            if loc:
                latitude = loc['latitude']
                longitude = loc['longitude']

        new_objects = []

        for x in objects:
            dlat = math.radians(x.latitude - latitude)
            dlon = math.radians(x.longitude - longitude)
            a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
                * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
            d = 6371 * c
           
            if d <= instance.radius:
                new_objects.append(x)

        objects = new_objects[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()
        
        context.update({'promos': objects})
        self.render_template = instance.template
        return context

class ShowEventsByDisciplineListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True
    allow_children = False
    cache = False
    module = ('Advertising')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionByDisciplineListingPlugin
    name = ("Event Promotion by Discipline Listing")

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        
        objects = objects.filter(disciplines__in=instance.disciplines.all()).distinct()[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()
        
        context.update({'promos': objects})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(ShowEventNearLocationPromotionListing)
plugin_pool.register_plugin(ShowEventNearUserPromotionListing)
plugin_pool.register_plugin(ShowEventsByDisciplineListingPlugin)
