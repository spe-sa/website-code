from HTMLParser import HTMLParser
from django.db import models

# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from filer.fields.image import FilerImageField
from django.conf import settings
from mainsite.widgets import ColorPickerWidget

# from django.core.urlresolvers import reverse
# from django.utils import six
# from django.utils.encoding import python_2_unicode_compatible, force_text
# from django.utils.functional import lazy
# from django.utils.translation import ugettext_lazy as _, string_concat

from cms.models import CMSPlugin
import logging

logger = logging.getLogger(__name__)


# DEFAULT_PAGE_TYPE = 'WWW'
# PAGE_TYPES = (
#     (DEFAULT_PAGE_TYPE, 'Web Page'),
#     ('JPT', 'Journal of Petroleum Technology'),
#     ('TWA', 'The Way Ahead'),
#     ('OGF', 'Oil and Gas Facilities'),
#     ('HSE', 'HSE Now'),
# )

# DEFAULT_PAGE_TEMPLATE = '3Column.html'
# PAGE_TEMPLATES = (
#    (DEFAULT_PAGE_TEMPLATE, 'Three Column'),
#    ('2Column.html', 'Two Column'),
#    ('1Column.html', 'Single Column'),
# )


# class PageTemplate(models.Model):
#    type_of_page = models.CharField(max_length=255, choices=PAGE_TYPES, default=DEFAULT_PAGE_TYPE)
#    template = models.CharField(max_length=255, choices=PAGE_TEMPLATES, default=DEFAULT_PAGE_TEMPLATE)

DEFAULT_TEXT_CLASS = 'tile-white'
TEXT_CLASS = (
    ('tile-alert', 'Alert Box'),
    ('tile-blue', 'Blue Box'),
    ('tile-greenbar', 'White Box - Green Bar'),
    ('tile-bluebar', 'White Box - Blue Bar'),
    (DEFAULT_TEXT_CLASS, 'White Box'),
)


DEFAULT_LINK_TARGET = '_blank'
LINK_TARGETS = (
    ('_self', 'Same Window'),
    (DEFAULT_LINK_TARGET, 'New Window'),
)


class ColorField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 10
        super(ColorField, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        kwargs['widget'] = ColorPickerWidget
        return super(ColorField, self).formfield(**kwargs)


class Web_Region(models.Model):
    region_code = models.CharField(max_length=15, unique=True)
    region_name = models.CharField(max_length=50, unique=True)
    is_visible = models.PositiveIntegerField(default=1)

    def __unicode__(self):
        buf = ""
        if self.region_name:
            buf += self.region_name
        else:
            buf += ""
        return buf

    class Meta:
        ordering = ['region_name']


class Web_Region_Country(models.Model):
    region = models.ForeignKey(Web_Region, null=True, on_delete=models.SET_NULL)
    country_UN = models.CharField("Country Code", max_length=25)

    def __unicode__(self):
        return self.country_UN


    class Meta:
        verbose_name = "Web Region Country"
        verbose_name_plural = "Web Region Countries"


class Regions(models.Model):
    region_code = models.CharField(max_length=15, unique=True)
    region_name = models.CharField(max_length=50, unique=True)

    def __unicode__(self):
        return self.region_code

    class Meta:
        ordering = ['region_code']
        verbose_name = "Region"


class Countries(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    country_ISO = models.CharField(max_length=2, unique=True)
    country_UN = models.CharField(max_length=3, unique=True)
    country_UN_number = models.PositiveIntegerField()
    country_dial_code = models.CharField(max_length=20)
    region = models.ForeignKey(Regions, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.country_name

    class Meta:
        ordering = ['country_name']
        verbose_name = "Country"
        verbose_name_plural = "Countries"


class Tier1Discipline(models.Model):
    # number = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=50, primary_key=True)
    crm_code = models.CharField(max_length=50, blank=True, null=True, verbose_name="CRM code")
    eva_code = models.CharField(max_length=100, blank=True, null=True, verbose_name="EVA code")
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Discipline"


class Topics(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Topic"


# # subscriptions: move to join table
# JPT subscription
# TWA subscription
# OGF subscription
# HSE subscription
class CustomerSubscription(models.Model):
    code = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=100)
    sort_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.description

    class Meta:
        ordering = ['sort_order', 'description']


# # classifications: move to join table
# committees | committee id
# bod | region?
# officer | committee id
# professional
# student
# grad_student
# yp
# lifetime -- also an award?
# new_grad_y1 | value?
# new_grad_y2 | value?
class CustomerClassification(models.Model):
    classificaton_types = (
        ('MEMBERSHIP', 'Membership'),
        ('ACHIEVEMENT', 'Achievement'),
        # ('SUBSCRIPTION', 'Subscription'),  QUESTION: should subscriptions be their own table or here?
    )
    code = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=20, choices=classificaton_types, default="MEMBERSHIP", blank=True, null=True)
    sort_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
    # code_value = models.CharField(max_length=100, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)

    def __unicode__(self):
        return str(self.description)
        # return self.description is not None and self.description or ''

    class Meta:
        ordering = ['sort_order', 'description']


# {     BIZTALK SYNC FIELDS FOR CUSTOMER
#   "CustomerName": "Mr  Adedeji O Ogunbela",
#   "CustomerNumber": "3354588",
#   "Source": "MBR",
#   "RecordType": "I",
#   "Birthday": "1979-04-01T19:00:00-05:00",
#   "Classification": "INDIVIDUAL",
#   "NamePrefix": "Mr.",
#   "FirstName": "Adedeji",
#   "MiddleName": "Olabode",
#   "LastName": "Ogunbela",
#   "Nickname": "Adedeji",
#   "FormalSalutation": "Mr. Adedeji O. Ogunbela",
#   "AllowEmail": "Y",
#   "Gender": "MALE",
#   "originalJoinDate": "2008-05-21T19:00:00-05:00",
#   "Address_1": null,
#   "Address_2": null,
#   "Address_3": null,
#   "Address_4_SPE": null,
#   "City": null,
#   "State": null,
#   "Country": null,
#   "Zip": null,
#   "PrimaryEmail": "dogunbela@hotmail.com",
#   "MembershipStatus": "Unpaid Member",
#   "Name_Suffix": null,
#   "paidThroughDate": null,
#   "contiguousJoinDate": null
# }


class Customer(models.Model):
    # __achievement_token = None
    # __achievement_bitmasks = {}
    # __achievement_values = {}

    id = models.CharField(max_length=12, primary_key=True)
    # name is assumed to be filled correctly by country etc
    name = models.CharField(max_length=300, blank=True, null=True)
    prefix = models.CharField(max_length=50, blank=True, null=True)
    suffix = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(db_index=True, max_length=80, blank=True, null=True)
    middle_name = models.CharField(max_length=60, blank=True, null=True)
    last_name = models.CharField(db_index=True, max_length=60, blank=True, null=True)
    nickname = models.CharField(max_length=80, blank=True, null=True)
    formal_salutation = models.CharField(max_length=180, blank=True, null=True)
    email = models.EmailField(db_index=True, blank=True, null=True)
    gender = models.CharField(max_length=12, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    address3 = models.CharField(max_length=255, blank=True, null=True)
    address4 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    zip = models.CharField(max_length=100, blank=True, null=True)
    allow_email = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    # membership_type = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)
    membership_status = models.CharField(max_length=50, blank=True, null=True)
    paid_through_date = models.DateField(blank=True, null=True)
    original_member_date = models.DateField(blank=True, null=True)
    continuous_member_date = models.DateField(blank=True, null=True)
    expected_grad_date = models.DateField(blank=True, null=True)

    primary_discipline = models.ForeignKey(Tier1Discipline, related_name="primary_customers", on_delete=models.SET_NULL,
                                           blank=True, null=True, limit_choices_to={'active': True})
    secondary_discipline = models.ForeignKey(Tier1Discipline, related_name="secondary_customers",
                                             on_delete=models.SET_NULL, blank=True, null=True, limit_choices_to={'active': True})
    subscriptions = models.ManyToManyField(CustomerSubscription, through='CustomerSubscriptionJoin',
                                           related_name="customers", blank=True)
    # classifications are internal classification to perform logic off of
    classifications = models.ManyToManyField(CustomerClassification, through='CustomerClassificationJoin',
                                             related_name='customers', blank=True)

    # ACHIEVEMENTS ARE NOW MERGED INTO CLASSIFICATIONS WITH TYPE 'ACHIEVEMENT'
    # # achievements are milestones that customers can achieve to gain notoriety
    # # (they are sortable and meant for display) subset of classifications for display
    # achievements = models.ManyToManyField(CustomerClassification, related_name='achievement_customers',
    #                                       blank=True)  # , through='CustomerAchievementJoin'

    # awards = models.ManyToManyField(CustomerAwards, blank=True, null=True) - TODO: implement later

    def has_achievement(self, achievement_key):
        return CustomerClassification.objects.filter(customers__id=self.id).filter(
            code=achievement_key).filter(type='ACHIEVEMENT').count() >= 1

    def has_classification(self, classification_key):
        return CustomerClassification.objects.filter(customers__id=self.id).filter(
            code=classification_key).count() >= 1

    def has_subscription(self, subscription_code):
        return CustomerSubscription.objects.filter(customers__id=self.id).filter(
            code=subscription_code).count() >= 1

    # derived from other stuff make def for each
    def greeting(self):
        if self.nickname:
            return self.nickname
        if self.first_name:
            return self.first_name
        if self.name:
            return self.name
        return "Guest"
    def is_officer(self):
        return self.has_classification("OFFICER")
    def has_committee(self):
        return self.has_classification("COMMITTEE")
    def is_board_member(self):
        return self.has_classification("BOD")
    def is_staff(self):
        return self.has_classification("STAFF")
    def is_professional_member(self):
        return self.membership_status == 'Paid Member'
        # return self.has_classification("PROFESSIONAL") or self.has_classification("LIFE")
    def is_student_member(self):
        return self.has_classification("STUDENT")

    # TODO: add any other is_ or has_ convenience methods for any join items below the same way

    # def set_achievement_token(self):
    #     # try to get from variable if prebuilt
    #     if not self.__achievement_token:
    #         # loop through all classifications; set the bit and then the bitmask and value dicts
    #         logger.error("private achievement_token not set building it...")
    #         self.__achievement_token = 3
    #         self.__achievement_bitmasks = {"OFFICER": 0x0001, "COMMITTEE": 0x0010, }
    #         self.__achievement_values = {"OFFICER": 9991099, "COMMITTEE": 9990123, }
    #     logging.error(str(self.__achievement_token) + " | " + str(self.__achievement_bitmasks) + " | " + str(
    #         self.__achievement_values))
    #
    def __unicode__(self):
        return self.id + " : " + self.name


class CustomerClassificationJoin(models.Model):
    customer = models.ForeignKey(Customer, related_name='classification_customer')
    classification = models.ForeignKey(CustomerClassification, related_name='classification_join')
    type = models.CharField(max_length=100, blank=True, null=True)
    value = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    crm_id = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s : %s" % (self.customer.id, self.classification.code)

    class Meta:
        db_table = 'mainsite_customer_classifications'


class CustomerSubscriptionJoin(models.Model):
    customer = models.ForeignKey(Customer, related_name='subscription_customer')
    subscription = models.ForeignKey(CustomerSubscription, related_name='subscription_join')
    value = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    crm_id = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return "%s : %s" % (self.customer.id, self.subscription.code)

    class Meta:
        db_table = 'mainsite_customer_subscriptions'


#
#
# # # Dena's Awards: move to join table
# # key_club
# # legion_of_honor
# # distinguished
# # honorary
# # century_club
# class CustomerAchievementJoin(models.Model):
#     customer = models.ForeignKey(Customer, related_name='achievement_customer')
#     classification = models.ForeignKey(CustomerClassification, related_name='achievement_join')
#     value = models.CharField(max_length=255, blank=True, null=True)
#     sort_order = models.PositiveSmallIntegerField(default=0, blank=False, null=False)
#
#     def __unicode__(self):
#         return "%s has achievement %s (%s)" % (self.customer, self.classification, self.value)


class AdSpeedZonePlugin(CMSPlugin):
    zid = models.PositiveIntegerField("Zone Id", blank=True, null=True)
    aid = models.PositiveIntegerField("Ad Id", blank=True, null=True)
    num = models.PositiveIntegerField("Number of Ads", blank=True, null=True)
    show_errors = models.BooleanField(default=False)

    # div_class = models.CharField(
    #     max_length=100,
    #     verbose_name="Wrapper Div Class",
    #     blank=True,
    #     null=True,
    # )

    def __unicode__(self):
        buf = "AdSpeed"
        if self.zid:
            buf += " Zone:" + str(self.zid)
        if self.aid:
            buf += " Ad:" + str(self.aid)
        if self.num:
            buf += " display " + str(self.num) + " Ads"
        return buf

    class Meta:
        ordering = ['zid', 'aid']


class TitleBarPlugin(CMSPlugin):
    title = models.CharField(max_length=100)
    # ADDED
    backcol = ColorField("Background Color", blank=True, null=True)
    textcol = ColorField("Text Color", blank=True, null=True)

    def __unicode__(self):
        return self.title


class MLStripper(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.fed = []

    def handle_data(self, d):
        self.fed.append(d)

    def get_data(self):
        return ''.join(self.fed)


def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()


class TextPlugin(CMSPlugin):
    txt = RichTextUploadingField(
        max_length=50000,
        help_text=u'Text'
    )
    cls = models.CharField(max_length=40, verbose_name="Class", choices=TEXT_CLASS, default=DEFAULT_TEXT_CLASS)

    def __unicode__(self):
        lbl = " - " + strip_tags(self.txt)
        return lbl[0:50]


class TileImgBack(CMSPlugin):
    ttl = models.CharField(blank=True, max_length=250, verbose_name="Title")
    txt = RichTextUploadingField(
        max_length=2000,
        help_text=u'Text Area'
    )
    lnk = models.URLField(max_length=250, verbose_name="Link")
    img = FilerImageField(blank=True, null=True, verbose_name=u'Background Image', related_name="background_picture")
    date = models.DateField(blank=True, null=True)
    linktarget = models.CharField(max_length=255, choices=LINK_TARGETS, default=DEFAULT_LINK_TARGET)

    def __unicode__(self):
        lbl = " - " + strip_tags(self.txt)
        return lbl[0:50]

    def get_absolute_url(self):
        # TODO: push this down to the SPEURLFIELD level and replace the URLFields above
        # replace all instances containing '//production_host_name/' with //env.hostname/ if we have env.hostname
        url = self.lnk
        if url:
            replacements = getattr(settings, "HOST_REPLACEMENTS", None)
            if replacements:
                for replace_host, new_host in replacements:
                    if url.find(replace_host) > -1:
                        url = url.replace(replace_host, new_host)
        return url


class MarketoFormPlugin(CMSPlugin):
    instructions = models.CharField(max_length=200, verbose_name="Instructions for form")
    thank_you = models.CharField(max_length=200, verbose_name="Confirmation text")
    marketo_form = models.PositiveIntegerField(verbose_name="Marketo form code")

    def __unicode__(self):
        return "Marketo Form: " + str(self.marketo_form)


class MarketoFormPluginNoThankYou(CMSPlugin):
    instructions = models.CharField(max_length=200, verbose_name="Instructions for form")
    marketo_form = models.PositiveIntegerField(verbose_name="Marketo form code")

    def __unicode__(self):
        return "Marketo Form with No Thank You: " + str(self.marketo_form)


class TimeZone(models.Model):
    code = models.CharField(max_length=12)
    description = models.CharField(max_length=120, blank=True, null=True)
    gmt_offset = models.IntegerField(default=0)

    def __unicode__(self):
        buff = str(self.code) + ": " + str(self.description) + ' [' + str(self.gmt_offset) + "]"
        return buff

    class Meta:
        ordering = ['code']