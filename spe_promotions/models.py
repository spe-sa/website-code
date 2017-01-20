import datetime

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from mainsite.models import Regions, Tier1Discipline, Web_Region, Topics, TimeZone, Customer
from spe_blog.models import Article
from spe_events.models import EventType

DEFAULT_PROMOTION_TYPE = 'generic'
PROMOTION_TYPE = (
    ('article', 'Article'),
    ('book', 'Book'),
    ('event', 'Event'),
    ('webinar', 'Webinar'),
    (DEFAULT_PROMOTION_TYPE, 'Generic'),
)


DEFAULT_PLUGIN_TEMPLATE = 'spe_promotions/plugins/carousel.html'
PLUGIN_TEMPLATES = (
    (DEFAULT_PLUGIN_TEMPLATE, 'Carousel'),
    ('spe_promotions/plugins/image_left.html', 'Image Left'),
    ('spe_promotions/plugins/image_text_below.html', 'Image Top, Text Below'),
    ('spe_promotions/plugins/overlay.html', 'Text Overlay'),
    ('spe_promotions/plugins/promotion_posts.html', 'Listing'),
)


DEFAULT_DISPLAY_TYPE = 'discipline'
DISPLAY_TYPE = (
    (DEFAULT_DISPLAY_TYPE, 'Events in Discipline'),
    ('region', 'Events in Region'),
)


class SimpleEventPromotion(models.Model):
    event = models.CharField(max_length=250)
    event_start_date = models.DateTimeField()
    event_end_date = models.DateTimeField()
    event_tz = models.ForeignKey(TimeZone, blank=True, null=True, on_delete=models.SET_NULL, editable=False)
    event_text_after = models.CharField(max_length=10, blank=True, null=True, verbose_name='Text after date (optional)', default="")
    event_text_date = models.CharField(max_length=25, verbose_name="Display Date Text (overrides actual date)", blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=50)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_promotion_picture")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date(2000, 1, 1), editable=False)
    event_type = models.ForeignKey(EventType, limit_choices_to={'active': True})
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], blank=True, null=True)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], blank=True,
                                  null=True)
    regions = models.ManyToManyField(Web_Region, blank=True)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True)
    start = models.DateField(verbose_name='Display Start Date')
    end = models.DateField(verbose_name='Display End Date')
    sponsored = models.BooleanField(default=False)
    click_url = models.URLField(verbose_name=u'Click Through External URL', blank=True, null=True)
    url = models.URLField(blank=True, null=True, editable=False)
    promotion_type = models.CharField(max_length=25, default="Event", editable=False)

    class Meta:
        ordering = ['-end', 'event']
        get_latest_by = ['end']

    def __unicode__(self):
        return "(" + self.start.strftime('%Y-%m-%d') + " - " + self.end.strftime('%Y-%m-%d') + ") - " + self.event_type.name + " - " + self.event

    def blank_timezone(self):
        self.event_tz = None
        self.save()
        return True


class SimpleEventNotLoggedInPromotion(models.Model):
    event = models.CharField(max_length=250, verbose_name='Title')
    event_start_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_end_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_tz = models.ForeignKey(TimeZone, blank=True, null=True, on_delete=models.SET_NULL, editable=False, db_constraint=False)
    event_text_date = models.CharField(max_length=25, verbose_name="Display Date Text (overrides actual date)", blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=50, editable=False, blank=True, null=True)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_notloggedin_promotion")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date(2000, 1, 1), editable=False)
    event_type = models.ForeignKey(EventType, limit_choices_to={'active': True}, editable=False, blank=True, null=True, db_constraint=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True}, editable=False, db_constraint=False)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], blank=True, null=True, editable=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], blank=True, null=True, editable=False)
    regions = models.ManyToManyField(Web_Region, blank=True, editable=False, db_constraint=False)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True, editable=False, db_constraint=False)
    start = models.DateField(verbose_name='Display Start Date')
    end = models.DateField(verbose_name='Display End Date')
    sponsored = models.BooleanField(default=False, editable=False)
    click_url = models.URLField(verbose_name=u'Click Through External URL', default="https://www.spe.org/appssecured/login/servlet/LoginServlet")
    url = models.URLField(blank=True, null=True, editable=False)
    promotion_type = models.CharField(max_length=25, default="Web-Not Logged In", editable=False)

    class Meta:
        verbose_name = 'Promotion for Not Logged In'
        verbose_name_plural = 'Promotions for Not Logged In'

    def __unicode__(self):
        return "(" + self.start.strftime('%Y-%m-%d') + " - " + self.end.strftime('%Y-%m-%d') + ") - " + self.event


class SimpleEventNonMemberPromotion(models.Model):
    event = models.CharField(max_length=250, verbose_name='Title')
    event_start_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_end_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_tz = models.ForeignKey(TimeZone, blank=True, null=True, on_delete=models.SET_NULL, editable=False, db_constraint=False)
    event_text_date = models.CharField(max_length=25, verbose_name="Display Date Text (overrides actual date)", blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=50, editable=False, blank=True, null=True)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_nonmember_promotion")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date(2000, 1, 1), editable=False)
    event_type = models.ForeignKey(EventType, limit_choices_to={'active': True}, editable=False, blank=True, null=True, db_constraint=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True}, editable=False, db_constraint=False)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], blank=True, null=True, editable=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], blank=True, null=True, editable=False)
    regions = models.ManyToManyField(Web_Region, blank=True, editable=False, db_constraint=False)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True, editable=False, db_constraint=False)
    start = models.DateField(verbose_name='Display Start Date')
    end = models.DateField(verbose_name='Display End Date')
    sponsored = models.BooleanField(default=False, editable=False)
    click_url = models.URLField(verbose_name=u'Click Through External URL', default="http://www.spe.org/join/")
    url = models.URLField(blank=True, null=True, editable=False)
    promotion_type = models.CharField(max_length=30, default="Membership-Non Member", editable=False)

    class Meta:
        verbose_name = 'Promotion for Non-Member'

    def __unicode__(self):
        return "(" + self.start.strftime('%Y-%m-%d') + " - " + self.end.strftime('%Y-%m-%d') + ") - " + self.event


class SimpleEventNoDisciplinePromotion(models.Model):
    event = models.CharField(max_length=250, verbose_name='Title')
    event_start_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_end_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_tz = models.ForeignKey(TimeZone, blank=True, null=True, on_delete=models.SET_NULL, editable=False, db_constraint=False)
    event_text_date = models.CharField(max_length=25, verbose_name="Display Date Text (overrides actual date)", blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=50, editable=False, blank=True, null=True)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_nodiscipline_promotion")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date(2000, 1, 1), editable=False)
    event_type = models.ForeignKey(EventType, limit_choices_to={'active': True}, editable=False, blank=True, null=True, db_constraint=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True}, editable=False, db_constraint=False)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], blank=True, null=True, editable=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], blank=True, null=True, editable=False)
    regions = models.ManyToManyField(Web_Region, blank=True, editable=False, db_constraint=False)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True, editable=False, db_constraint=False)
    start = models.DateField(verbose_name='Display Start Date')
    end = models.DateField(verbose_name='Display End Date')
    sponsored = models.BooleanField(default=False, editable=False)
    click_url = models.URLField(verbose_name=u'Click Through External URL', default="https://www.spe.org/member/access/TechnicalDisciplines")
    url = models.URLField(blank=True, null=True, editable=False)
    promotion_type = models.CharField(max_length=30, default="Membership-No Discipline", editable=False)

    class Meta:
        verbose_name = 'Promotion for Missing Discipline'

    def __unicode__(self):
        return "(" + self.start.strftime('%Y-%m-%d') + " - " + self.end.strftime('%Y-%m-%d') + ") - " + self.event


class SimpleEventNoAddressPromotion(models.Model):
    event = models.CharField(max_length=250, verbose_name='Title')
    event_start_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_end_date = models.DateTimeField(editable=False, blank=True, null=True)
    event_tz = models.ForeignKey(TimeZone, blank=True, null=True, on_delete=models.SET_NULL, editable=False, db_constraint=False)
    event_text_date = models.CharField(max_length=25, verbose_name="Display Date Text (overrides actual date)", blank=True, null=True, editable=False)
    event_location = models.CharField(max_length=50, editable=False, blank=True, null=True)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_noaddress_promotion")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date(2000, 1, 1), editable=False)
    event_type = models.ForeignKey(EventType, limit_choices_to={'active': True}, editable=False, blank=True, null=True, db_constraint=False)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True}, editable=False, db_constraint=False)
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)], blank=True, null=True, editable=False)
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)], blank=True, null=True, editable=False)
    regions = models.ManyToManyField(Web_Region, blank=True, editable=False, db_constraint=False)
    topics = models.ManyToManyField(Topics, verbose_name="Topics of Interest", blank=True, editable=False, db_constraint=False)
    start = models.DateField(verbose_name='Display Start Date')
    end = models.DateField(verbose_name='Display End Date')
    sponsored = models.BooleanField(default=False, editable=False)
    click_url = models.URLField(verbose_name=u'Click Through External URL', default="https://www.spe.org/member/access/Address")
    url = models.URLField(blank=True, null=True, editable=False)
    promotion_type = models.CharField(max_length=25, default="Membership-No Address", editable=False)

    class Meta:
        verbose_name = 'Promotion for Missing Address'

    def __unicode__(self):
        return "(" + self.start.strftime('%Y-%m-%d') + " - " + self.end.strftime('%Y-%m-%d') + ") - " + self.event


class PromotionsEventClicks(models.Model):
    promotion_title = models.CharField(max_length=250, verbose_name='Title')
    promotion_type = models.CharField(max_length=25)
    promotion_id = models.PositiveIntegerField()
    time = models.DateTimeField()
    ip = models.CharField(max_length=17)
    vid = models.CharField(max_length=60, default='unknown')
    customer_id = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = 'Promotion Clicks'
        verbose_name_plural = 'Promotions Clicks'

    def __unicode__(self):
        return self.promotion_title


# class SimpleEventNonMemberMessage(models.Model):
#     promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Non-Member or Member Who Has Not Logged In')
#
#     class Meta:
#         verbose_name = 'Promotion for Non-Member or Member Not Logged In'
#
#     def __unicode__(self):
#         return self.promotion.event


# class SimpleEventMemberMissingDisciplineMessage(models.Model):
#     promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Member with no Primary Discipline')
#
#     class Meta:
#         verbose_name = 'Promotion for Member with No Primary Discipline'
#
#     def __unicode__(self):
#         return self.promotion.event


# class SimpleEventMemberMissingRegionMessage(models.Model):
#     promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Member with no Region')
#
#     class Meta:
#         verbose_name = 'Promotion for Member with No Address'
#
#     def __unicode__(self):
#         return self.promotion.event


class EventPromotionByDisciplineListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (disciplines: %s)" % ', '.join([a.name for a in self.disciplines.all()])
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()
        self.event_type = old_instance.event_type.all()


class EventPromotionByTopicListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    topics = models.ManyToManyField(Topics, blank=True, limit_choices_to={'active': True})
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (topics: %s)" % ', '.join([a.name for a in self.topics.all()])
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.topics = old_instance.topics.all()
        self.event_type = old_instance.event_type.all()


class EventPromotionByRegionListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    regions = models.ManyToManyField(Web_Region, blank=True, limit_choices_to={'is_visible': True})
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})


    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (regions: %s)" % ', '.join([a.region_name for a in self.regions.all()])
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.regions = old_instance.regions.all()
        self.event_type = old_instance.event_type.all()


class EventPromotionSelectionPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    promotions = models.ManyToManyField(SimpleEventPromotion)

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += "%s, " % ', '.join([a.event for a in self.promotions.all()])
        return buf

    def copy_relations(self, old_instance):
        self.promotions = old_instance.promotions.all()


class EventPromotionInUserRegionListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})


    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.event_type = old_instance.event_type.all()


class EventForMemberListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    show = models.CharField(max_length=255, choices=DISPLAY_TYPE, default=DEFAULT_DISPLAY_TYPE)
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})


    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        dictionary = dict(DISPLAY_TYPE)
        buf += dictionary[self.show]
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.event_type = old_instance.event_type.all()


class UpcomingEventPromotionPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    disciplines = models.ManyToManyField(Tier1Discipline, limit_choices_to={'active': True}, db_constraint=False)
    regions = models.ManyToManyField(Web_Region, limit_choices_to={'is_visible': True})
    event_type = models.ManyToManyField(EventType, limit_choices_to={'active': True})


    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (disciplines: %s)" % ', '.join([a.name for a in self.disciplines.all()])
        buf += " (regions: %s)" % ', '.join([a.region_name for a in self.regions.all()])
        buf += " (event type: %s)" % ', '.join([a.name for a in self.event_type.all()])
        return buf

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()
        self.regions = old_instance.regions.all()
        self.event_type = old_instance.event_type.all()