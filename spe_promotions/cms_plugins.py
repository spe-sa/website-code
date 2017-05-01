import datetime
from itertools import chain

# from netaddr import IPAddress

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from mainsite.common import (
    get_visitor,
)
from mainsite.models import Web_Region_Country
from mainsite.common import getRegion

from .forms import SimplePromotionsSelectionForm, SimpleMembershipPromotionSelectionForm
from .models import (
    SimpleEventPromotion,
    SimpleEventNotLoggedInPromotion,
    SimpleEventNoDisciplinePromotion,
    SimpleEventNoAddressPromotion,
    EventPromotionByDisciplineListingPlugin,
    EventPromotionByTopicListingPlugin,
    EventPromotionByRegionListingPlugin,
    EventPromotionSelectionPlugin,
    EventPromotionInUserRegionListingPlugin,
    EventForMemberListingPlugin,
    UpcomingEventPromotionPlugin,
    SimpleMembershipPromotion,
    MembershipPromotionSelectionPlugin,
)

exclude_agents = ['bot', 'spider', 'crawl', 'search']


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

        request = context.get('request')
        #         ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
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

        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
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

        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
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

        request = context.get('request')
        #         ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
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

        region = getRegion(context)

        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today, regions=region,
                                                      event_type=instance.event_type.all()).order_by('last_impression')[
                  :instance.count]

        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
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

        no_discipline_promotions = SimpleEventNoDisciplinePromotion.objects.filter(start__lte=today,
                                                                                   end__gte=today).order_by(
            'last_impression')[:1]
        no_discipline = False

        no_region_promotions = SimpleEventNoAddressPromotion.objects.filter(start__lte=today, end__gte=today).order_by(
            'last_impression')[:1]
        no_region = False

        not_logged_in_promotions = SimpleEventNotLoggedInPromotion.objects.filter(start__lte=today,
                                                                                  end__gte=today).order_by(
            'last_impression')[:1]
        not_logged_in = False

        objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')

        if visitor:
            # The Member is Logged In
            if instance.show == 'discipline':
                if visitor.primary_discipline:
                    if visitor.primary_discipline.active:
                        # Member - Primary Discipline Available
                        objects = objects.filter(disciplines=visitor.primary_discipline,
                                                 event_type=instance.event_type.all())
                        # If a Secondary Discipline is Available Append Events for that Discipline
                        if visitor.secondary_discipline:
                            append_objects = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today,
                                                                                 disciplines=visitor.secondary_discipline,
                                                                                 event_type=instance.event_type.all()).order_by(
                                'last_impression')
                            objects = list(chain(objects, append_objects))
                    else:
                        # Member - Primary Discipline is Obsolete
                        prepend_object = no_discipline_promotions
                        no_discipline = True
                        # Drop Back to Member Location then Browser Location (if selected)
                        if visitor.country:
                            # Member - Region Available
                            try:
                                region = Web_Region_Country.objects.get(country_UN=visitor.country).region
                            except Web_Region_Country.DoesNotExist:
                                region = Web_Region_Country.objects.get(country_UN='USA').region
                        else:
                            region = getRegion(context)
                        objects = objects.filter(regions=region, event_type=instance.event_type.all())
                        objects = list(chain(prepend_object, objects))
                else:
                    # Member - No Primary Discipline Available
                    prepend_object = no_discipline_promotions
                    no_discipline = True
                    # Drop Back to Member Location then Browser Location (if selected)
                    if visitor.country:
                        # Member - Region Available
                        try:
                            region = Web_Region_Country.objects.get(country_UN=visitor.country).region
                        except Web_Region_Country.DoesNotExist:
                            region = Web_Region_Country.objects.get(country_UN='USA').region
                    else:
                        region = getRegion(context)
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
                    prepend_object = no_region_promotions
                    no_region = True
                    # always use browsing user's location
                    region = getRegion(context)
                    objects = objects.filter(regions=region, event_type=instance.event_type.all())
                    objects = list(chain(prepend_object, objects))
        else:
            # Member Not Logged In
            prepend_object = not_logged_in_promotions
            not_logged_in = True
            # If Browsing Location Selected for Non-Member or Member Not Logged In, Create New Promotions List
            region = getRegion(context)
            objects = objects.filter(regions=region, event_type=instance.event_type.all())
            objects = list(chain(prepend_object, objects))

        objects = objects[:instance.count]
        i = 0
        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        #         ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            if i == 0:
                if no_discipline:
                    x.url = "/en/promotion/no_discipline/" + str(x.id) + "/"
                elif no_region:
                    x.url = "/en/promotion/no_region/" + str(x.id) + "/"
                elif not_logged_in:
                    x.url = "/en/promotion/not_logged_in/" + str(x.id) + "/"
            i += 1
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
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
                                                      event_start_date__gte=today).order_by(
            'event_start_date').distinct()[:instance.count]

        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        # ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/event/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        if instance.more_url:
            context.update({'more_url': instance.more_url})
            context.update({'more_text': instance.more_text})
        self.render_template = instance.template
        return context


class ShowMembershipListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Membership Promotions'
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = MembershipPromotionSelectionPlugin
    name = "Membership Promotion Listing - Selected Promotions"
    form = SimpleMembershipPromotionSelectionForm

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = SimpleMembershipPromotion.objects.filter(start__lte=today, end__gte=today,
                                                           id__in=instance.promotions.all()).order_by(
            'last_impression').distinct()

        request = context.get('request')
        #        ip = request.META.get('HTTP_X_REAL_IP', '192.168.1.1')
        # ip = get_ip(request)
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        for x in objects:
            x.url = "/en/promotion/membership/" + str(x.id) + "/"
            # if not request.user.is_authenticated() and not IPAddress(ip).is_private() and not any(
            if not request.user.is_authenticated() and not request.variables['is_local_ip'] and not any(
                    [y in user_agent.lower() for y in exclude_agents]):
                x.last_impression = datetime.datetime.now()
                x.impressions += 1
                x.save()

        context.update({'promos': objects})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(ShowEventsByDisciplineListingPlugin)
plugin_pool.register_plugin(ShowEventsByTopicListingPlugin)
plugin_pool.register_plugin(ShowEventsByRegionListingPlugin)
plugin_pool.register_plugin(ShowEventsListingPlugin)
plugin_pool.register_plugin(ShowEventInUserRegionPromotionListing)
plugin_pool.register_plugin(ShowEventsForMemberPlugin)
plugin_pool.register_plugin(ShowUpcomingEventsListingPlugin)
plugin_pool.register_plugin(ShowMembershipListingPlugin)
