import datetime
from itertools import chain

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.contrib.gis.geoip import GeoIP

from mainsite.context_processors.spe_context import (
    get_visitor,
)
from mainsite.models import Web_Region_Country
from mainsite.common import getRegion

from .forms import SimplePromotionsSelectionForm
from .models import (
    SimpleEventPromotion,
    # EventPromotionNearLocationListingPlugin,
    # EventPromotionNearUserListingPlugin,
    EventPromotionByDisciplineListingPlugin,
    EventPromotionByTopicListingPlugin,
    EventPromotionByRegionListingPlugin,
    EventPromotionSelectionPlugin,
    EventPromotionInUserRegionListingPlugin,
    EventForMemberListingPlugin,
    UpcomingEventPromotionPlugin,
    SimpleEventNonMemberMessage,
    SimpleEventMemberMissingDisciplineMessage,
    SimpleEventMemberMissingRegionMessage,
)


# from spe_events.models import EventType


# class ShowPromotionListingPlugin(CMSPluginBase):
#     class Meta:
#         abstract = True
#     allow_children = False
#     cache = False
#     module = ('Event Promotions')
#     render_template = 'spe_blog/plugins/image_left.html'
#     text_enabled = False
#     model = SimpleEventPromotionListingPlugin
#     name = ("Promotion Listing")
#
#     def render(self, context, instance, placeholder):
#         today = datetime.date.today()
#         objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
#
#         if instance.disciplines.all():
#             objects = objects.filter(disciplines__in=instance.disciplines.all())
#
#         request = context['request']
#         g = GeoIP()
#         # ip = context['request'].META.get('REMOTE_ADDR', None)
#         ip = context['request'].META.get('HTTP_X_REAL_IP', None)
#         if not ip:
#             ip = '192.152.183.80'
#         if ip:
#             loc = g.city(ip)
#             if loc:
#                 latitude = loc['latitude']
#                 longitude = loc['longitude']
#
#         new_objects = []
#
#         for x in objects:
#             dlat = math.radians(x.latitude - latitude)
#             dlon = math.radians(x.longitude - longitude)
#             a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
#                 * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
#             c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#             d = 6371 * c
#
#             if d <= instance.radius:
#                 new_objects.append(x)
#
#         objects = new_objects[:instance.count]
#
#         for x in objects:
#             x.url = "/promotion/event/" + str(x.id) + "/"
#             x.last_impression = datetime.datetime.now()
#             x.impressions += 1
#             x.save()
#
#         context.update({'promos': objects})
#         self.render_template = instance.template
#         return context

# class ShowEventNearLocationPromotionListing(CMSPluginBase):
#     class Meta:
#         abstract = True
#     allow_children = False
#     cache = False
#     module = ('Event Promotions')
#     render_template = 'spe_blog/plugins/image_left.html'
#     text_enabled = False
#     model = EventPromotionNearLocationListingPlugin
#     name = ("Event Promotion Listing Within Radius of Latitude and Longitude")
#
#     def render(self, context, instance, placeholder):
#         today = datetime.date.today()
#         objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
#
#         new_objects = []
#
#         for x in objects:
#             dlat = math.radians(x.latitude - instance.latitude)
#             dlon = math.radians(x.longitude - instance.longitude)
#             a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(instance.latitude)) \
#                 * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
#             c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#             d = 6371 * c
#
#             if d <= instance.radius:
#                 new_objects.append(x)
#
#         objects = new_objects[:instance.count]
#
#         for x in objects:
#             x.url = "/promotion/event/" + str(x.id) + "/"
#             x.last_impression = datetime.datetime.now()
#             x.impressions += 1
#             x.save()
#
#         context.update({'promos': objects})
#         self.render_template = instance.template
#         return context

# class ShowEventNearUserPromotionListing(CMSPluginBase):
#     class Meta:
#         abstract = True
#     allow_children = False
#     cache = False
#     module = ('Event Promotions')
#     render_template = 'spe_blog/plugins/image_left.html'
#     text_enabled = False
#     model = EventPromotionNearUserListingPlugin
#     name = ("Event Promotion Listing Within Radius of Browsed From Location")
#
#     def render(self, context, instance, placeholder):
#         today = datetime.date.today()
#         objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
#
#         request = context['request']
#         g = GeoIP()
#         # ip = context['request'].META.get('REMOTE_ADDR', None)
#         ip = context['request'].META.get('HTTP_X_REAL_IP', None)
#         if not ip:
#             ip = '192.152.183.80'
#         if ip:
#             loc = g.city(ip)
#             if loc:
#                 latitude = loc['latitude']
#                 longitude = loc['longitude']
#
#         new_objects = []
#
#         for x in objects:
#             dlat = math.radians(x.latitude - latitude)
#             dlon = math.radians(x.longitude - longitude)
#             a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(latitude)) \
#                 * math.cos(math.radians(x.latitude)) * math.sin(dlon/2) * math.sin(dlon/2)
#             c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
#             d = 6371 * c
#
#             if d <= instance.radius:
#                 new_objects.append(x)
#
#         objects = new_objects[:instance.count]
#
#         for x in objects:
#             x.url = "/promotion/event/" + str(x.id) + "/"
#             x.last_impression = datetime.datetime.now()
#             x.impressions += 1
#             x.save()
#
#         context.update({'promos': objects})
#         self.render_template = instance.template
#         return context

class ShowEventsByDisciplineListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionByDisciplineListingPlugin
    name = "Event Promotion Listing by Discipline"

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')

        objects = objects.filter(disciplines__in=instance.disciplines.all(),
                                 event_type=instance.event_type.all()).distinct()[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowEventsByTopicListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionByTopicListingPlugin
    name = "Event Promotion Listing by Topics"

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')

        objects = objects.filter(topics__in=instance.topics.all(), event_type=instance.event_type.all()).distinct()[
                  :instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowEventsByRegionListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionByRegionListingPlugin
    name = "Event Promotion Listing by Region"

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')

        objects = objects.filter(regions__in=instance.regions.all(), event_type=instance.event_type.all()).distinct()[
                  :instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowEventsListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionSelectionPlugin
    name = "Event Promotion Listing - Selected Events"
    form = SimplePromotionsSelectionForm

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                      id__in=instance.promotions.all()).order_by(
            'last_impression').distinct()

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowEventInUserRegionPromotionListing(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventPromotionInUserRegionListingPlugin
    name = "Event Promotion Listing by Region Browsed From"

    def render(self, context, instance, placeholder):
        today = datetime.date.today()

        region = getRegion(context, 'USA')

        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today, regions=region,
                                                      event_type=instance.event_type.all()).order_by('last_impression')[
                  :instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowEventsForMemberPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = EventForMemberListingPlugin
    name = "Personalized Event Promotion Listing"

    def render(self, context, instance, placeholder):
        request = context.get('request')
        visitor = get_visitor(request)

        # Get default list of active promotions sorted by round robin placement and exclude special promotions
        today = datetime.date.today()
        # objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        no_discipline_promotions = SimpleEventMemberMissingDisciplineMessage.objects.all()
        ids_to_exclude = [o for o in no_discipline_promotions]
        no_region_promotions = SimpleEventMemberMissingRegionMessage.objects.all()
        ids_to_exclude += [o for o in no_region_promotions]
        non_member_promotions = SimpleEventNonMemberMessage.objects.all()
        ids_to_exclude += [o for o in non_member_promotions]
        exclude_id = [x.promotion.id for x in ids_to_exclude]
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).exclude(
            id__in=exclude_id).order_by('last_impression')
        # append_objects = objects

        if visitor:
            # The Member is Logged In
            if instance.show == 'discipline':
                if visitor.primary_discipline:
                    # Member - Primary Discipline Available
                    objects = objects.filter(disciplines=visitor.primary_discipline,
                                             event_type=instance.event_type.all())
                    # If a Secondary Discipline is Available Append Events for that Discipline
                    if visitor.secondary_discipline:
                        append_objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                            disciplines=visitor.secondary_discipline, event_type=instance.event_type.all()).exclude(id__in=exclude_id).order_by('last_impression')
                        objects = list(chain(objects, append_objects))
                else:
                    # Member - No Primary Discipline Available
                    prepend_object = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                                         id__in=no_discipline_promotions.values(
                                                                             'promotion')).order_by('last_impression')[
                                     :1]
                    # Drop Back to Member Location then Browser Location (if selected)
                    if visitor.country:
                        # Member - Region Available
                        try:
                            region = Web_Region_Country.objects.get(country_UN=visitor.country).region
                        except Web_Region_Country.DoesNotExist:
                            region = Web_Region_Country.objects.get(country_UN='USA').region
                    else:
                        region = getRegion(context, 'USA')
                    objects = objects.filter(regions=region, event_type=instance.event_type.all())
                    objects = list(chain(prepend_object, objects))

            if instance.show == 'region':
                # Member - Region Available
                if visitor.country:
                    # Member - Region Available
                    try:
                        region = Web_Region_Country.objects.get(country_UN=visitor.country).region
                    except Web_Region_Country.DoesNotExist:
                        region = Web_Region_Country.objects.get(country_UN='USA').region
                    objects = objects.filter(regions=region, event_type=instance.event_type.all()).distinct()
                else:
                    # Member - No Region Available
                    prepend_object = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                                         id__in=no_region_promotions.values(
                                                                             'promotion')).order_by('last_impression')[
                                     :1]
                    # always use browsing user's location
                    region = getRegion(context, 'USA')
                    objects = objects.filter(regions=region, event_type=instance.event_type.all())
                    objects = list(chain(prepend_object, objects))
        else:
            # Non-Member or Member Not Logged In
            prepend_object = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                                 id__in=non_member_promotions.values(
                                                                     'promotion')).order_by('last_impression')[
                             :1]
            # If Browsing Location Selected for Non-Member or Member Not Logged In, Create New Promotions List
            region = getRegion(context, 'USA')
            objects = objects.filter(regions=region, event_type=instance.event_type.all())
            objects = list(chain(prepend_object, objects))

        objects = objects[:instance.count]
        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


class ShowUpcomingEventsListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Event Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = UpcomingEventPromotionPlugin
    name = "List Upcoming Events"

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                      disciplines__in=instance.disciplines.all(),
                                                      event_type__in=instance.event_type.all(),
                                                      regions__in=instance.regions.all(),
                                                      event_start_date__gte=today).order_by('event_start_date').distinct()[:instance.count]

        for x in objects:
            x.url = "/promotion/event/" + str(x.id) + "/"
            x.last_impression = datetime.datetime.now()
            x.impressions += 1
            x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


# plugin_pool.register_plugin(ShowEventNearLocationPromotionListing)
# plugin_pool.register_plugin(ShowEventNearUserPromotionListing)
plugin_pool.register_plugin(ShowEventsByDisciplineListingPlugin)
plugin_pool.register_plugin(ShowEventsByTopicListingPlugin)
plugin_pool.register_plugin(ShowEventsByRegionListingPlugin)
plugin_pool.register_plugin(ShowEventsListingPlugin)
plugin_pool.register_plugin(ShowEventInUserRegionPromotionListing)
plugin_pool.register_plugin(ShowEventsForMemberPlugin)
plugin_pool.register_plugin(ShowUpcomingEventsListingPlugin)
