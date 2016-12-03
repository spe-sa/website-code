import datetime
from django.db import models
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from cms.models.fields import PageField
from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from mainsite.models import Regions, Tier1Discipline, Web_Region, Topics
from spe_blog.models import Article

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
    ('spe_promotions/plugins/jb_carousel.html', 'JB Carousel')
)


DEFAULT_DISPLAY_TYPE = 'discipline'
DISPLAY_TYPE = (
    (DEFAULT_DISPLAY_TYPE, 'Events in Discipline Regardless of Region'),
    ('region', 'Regional Events Only'),
    ('disinreg', 'Events in Discipline in Region Only'),
    ('displusreg', 'Events in Discipline Supplemented by Regional Events')
)


#class Promotion(models.Model):
#    title = models.CharField(max_length=250)
#    teaser = RichTextUploadingField(
#        max_length=300,
#    )
#    # slug = models.SlugField(max_length=100, help_text='SEO Friendly name that is unique for use in URL', )
#    is_logo = models.BooleanField(verbose_name='LOGO', default=False)
#    picture = FilerImageField(verbose_name=u'Picture for article', related_name="promotion_picture")
#    picture_alternate = models.CharField(max_length=250, blank=True, null=True, verbose_name=u'Picture alternate text')
#    hits = models.PositiveIntegerField(default=0, editable=False)
#    impressions = models.PositiveIntegerField(default=0, editable=False)
#    last_impression = models.DateTimeField(default=datetime.date.today() + datetime.timedelta(-30), editable=False)
#    promotion_type = models.CharField(max_length=40, verbose_name="Promotion Type", choices=PROMOTION_TYPE,
#                                      default=DEFAULT_PROMOTION_TYPE)
#    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})
#    regions = models.ManyToManyField(Regions, blank=True)
#    start = models.DateField(verbose_name='Start Date')
#    end = models.DateField(verbose_name='End Date')
#    click_page = PageField(verbose_name="Click Through Page", blank=True, null=True, on_delete=models.SET_NULL)
#    click_url = models.URLField(verbose_name=u'Click Through External URL', blank=True, null=True)
#    article = models.ForeignKey(Article, blank=True, null=True)
#    sponsored = models.BooleanField(default=False)
#    url = models.URLField(blank=True, null=True, editable=False)

#    class Meta:
#        ordering = ['-end', 'title']
#        get_latest_by = ['end']

#    def __unicode__(self):
#        return self.title


class PromotionListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    promotion_type = models.CharField(max_length=40, verbose_name="Promotion Type", choices=PROMOTION_TYPE,
                                      default=DEFAULT_PROMOTION_TYPE)
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})
    regions = models.ManyToManyField(Regions, blank=True)

    def __unicode__(self):
        buf = str(self.count) + " - " + self.promotion_type
        buf += " (disciplines: %s)" % ', '.join([a.code for a in self.disciplines.all()])
        buf += " (regions: %s)" % ', '.join([a.region_code for a in self.regions.all()])
        return buf

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()
        self.regions = old_instance.regions.all()


class SimpleEventPromotion(models.Model):
    event = models.CharField(max_length=250)
    event_date = models.DateField(verbose_name='Event Date')
    event_location = models.CharField(max_length=50)
    teaser = RichTextUploadingField(
        max_length=300,
    )
    picture = FilerImageField(verbose_name=u'Picture for event promotion', related_name="simple_promotion_picture")
    hits = models.PositiveIntegerField(default=0, editable=False)
    impressions = models.PositiveIntegerField(default=0, editable=False)
    last_impression = models.DateTimeField(default=datetime.date.today() + datetime.timedelta(-30), editable=False)
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

    class Meta:
        ordering = ['-end', 'event']
        get_latest_by = ['end']

    def __unicode__(self):
        return self.event


class SimpleEventNonMemberMessage(models.Model):
    promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Non-Member or Member Who Has Not Logged In')

    class Meta:
        verbose_name = 'Promotion for Non-Member or Member Not Logged In'

    def __unicode__(self):
        return self.promotion.event


class SimpleEventMemberMissingDisciplineMessage(models.Model):
    promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Member with no Primary Discipline')

    class Meta:
        verbose_name = 'Promotion for Member with No Primary Discipline'

    def __unicode__(self):
        return self.promotion.event


class SimpleEventMemberMissingRegionMessage(models.Model):
    promotion = models.ForeignKey(SimpleEventPromotion, verbose_name='Promotion for Member with no Region')

    class Meta:
        verbose_name = 'Promotion for Member with No Address'

    def __unicode__(self):
        return self.promotion.event


class SimpleEventPromotionListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})
    radius = models.FloatField(validators=[MinValueValidator(0.1)])

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (disciplines: %s)" % ', '.join([a.code for a in self.disciplines.all()])
        buf += " within a radius of " + str(self.radius)
        return buf

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()


class EventPromotionNearLocationListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    latitude = models.FloatField(validators=[MinValueValidator(-90.0), MaxValueValidator(90.0)])
    longitude = models.FloatField(validators=[MinValueValidator(-180.0), MaxValueValidator(180.0)])
    radius = models.FloatField(validators=[MinValueValidator(0.1)])

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - near (" + str(self.latitude) + "," + str(self.longitude) + ")"
        buf += " within a radius of " + str(self.radius)
        return buf


class EventPromotionNearUserListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    radius = models.FloatField(validators=[MinValueValidator(0.1)])

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - within a radius of " + str(self.radius)
        return buf


class EventPromotionByDisciplineListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    disciplines = models.ManyToManyField(Tier1Discipline, blank=True, limit_choices_to={'active': True})

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (disciplines: %s)" % ', '.join([a.code for a in self.disciplines.all()])
        return buf

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()


class EventPromotionByTopicListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    topics = models.ManyToManyField(Topics, blank=True, limit_choices_to={'active': True})

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (topics: %s)" % ', '.join([a.name for a in self.topics.all()])
        return buf

    def copy_relations(self, old_instance):
        self.topics = old_instance.topics.all()


class EventPromotionByRegionListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    regions = models.ManyToManyField(Web_Region, blank=True, limit_choices_to={'is_visible': True})

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        buf += " (regions: %s)" % ', '.join([a.region_code for a in self.regions.all()])
        return buf

    def copy_relations(self, old_instance):
        self.regions = old_instance.regions.all()


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

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count)
        return buf


class EventForMemberListingPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=PLUGIN_TEMPLATES, default=DEFAULT_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Promotions')
    show = models.CharField(max_length=255, choices=DISPLAY_TYPE, default=DEFAULT_DISPLAY_TYPE)
    use_browsing_location = models.BooleanField(default=True, verbose_name='Use Browsing Location if Not Logged In')

    def __unicode__(self):
        dictionary = dict(PLUGIN_TEMPLATES)
        buf = " - " + dictionary[self.template] + " - "
        buf += str(self.count) + " - "
        dictionary = dict(DISPLAY_TYPE)
        buf += dictionary[self.show]
        return buf