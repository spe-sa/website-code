from HTMLParser import HTMLParser
from django.db import models

from ckeditor.fields import RichTextField
# from ckeditor_uploader.fields import RichTextUploadingField

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


class Tier1Discipline(models.Model):
    number = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=3, primary_key=True)
    long_code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = "Discipline"

class Topics(models.Model):
    discipline = models.ForeignKey(Tier1Discipline, verbose_name="Discipline")
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        buf = self.discipline.name + " - " + self.name
        return buf

    class Meta:
        ordering = ['name']
        verbose_name = "Topic"


# # subscriptions: move to join table
# JPT subscription
# TWA subscription
# OGF subscription
# HSE subscription
class CustomerSubscription(models.Model):
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)


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
    code = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    value = models.CharField(max_length=150)


# # Dena's Awards: move to join table
# key_club
# legion_of_honor
# distinguished
# honorary
# century_club
class CustomerAchievements(CustomerClassification):
    sort_order = models.PositiveSmallIntegerField(blank=True, null=True)
    weight = models.PositiveSmallIntegerField(blank=True, null=True)


class Customer(models.Model):
    __achievement_token = None
    __achievement_bitmasks = {}
    __achievement_values = {}

    customer_id = models.CharField(max_length=12, primary_key=True)
    # name is assumed to be filled correctly by country etc
    name = models.CharField(max_length=100)
    email = models.EmailField()
    primary_discipline = models.ForeignKey(Tier1Discipline, related_name="primary_customers", blank=True, null=True)
    secondary_discipline = models.ForeignKey(Tier1Discipline, related_name="secondary_customers", blank=True, null=True)
    # membership_type = models.CharField(max_length=30)
    last_year_paid = models.PositiveIntegerField(blank=True, null=True)
    first_member_date = models.DateField(blank=True, null=True)
    continuous_start_date = models.DateField(blank=True, null=True)
    expected_grad_year = models.DateField(blank=True, null=True)
    subscriptions = models.ManyToManyField(CustomerSubscription, blank=True)
    # classifications are internal classification to perform logic off of
    classifications = models.ManyToManyField(CustomerClassification, related_name="classification_customers",
                                             blank=True)
    # achievements are milestones that customers can achieve to gain notoriety
    # (they are sortable and meant for display) subset of classifications for display
    achievements = models.ManyToManyField(CustomerAchievements, related_name="achievement_customers", blank=True)

    # awards = models.ManyToManyField(CustomerAwards, blank=True, null=True) - TODO: implement later

    # derived from other stuff make def for each
    def is_officer(self):
        if not self.__achievement_token:
            self.set_achievement_token()

        return self.__achievement_token & self.__achievement_bitmasks.get("OFFICER")

    def has_committee(self):
        return self.classifications.filter(code__exact="COMMITTEE").count >= 1

    def is_board_member(self):
        return self.classifications.filter(code__exact="BOD").count >= 1

    # TODO: add any other is_ or has_ convenience methods for any join items below the same way

    def set_achievement_token(self):
        # try to get from variable if prebuilt
        if not self.__achievement_token:
            # loop through all classifications; set the bit and then the bitmask and value dicts
            logger.error("private achievement_token not set building it...")
            self.__achievement_token = 3
            self.__achievement_bitmasks = {"OFFICER": 0x0001, "COMMITTEE": 0x0010, }
            self.__achievement_values = {"OFFICER": 9991099, "COMMITTEE": 9990123, }
        logging.error(str(self.__achievement_token) + " | " + str(self.__achievement_bitmasks) + " | " + str(
            self.__achievement_values))

    def __unicode__(self):
        return self.customer_id


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
    txt = RichTextField(max_length=1000, verbose_name="Text")

    def __unicode__(self):
        lbl = " - " + strip_tags(self.txt)
        return lbl[0:50]


class TextWithClass(CMSPlugin):
    txt = RichTextField(max_length=1000, verbose_name="Text")
    cls = models.CharField(max_length=40, verbose_name="Class")

    def __unicode__(self):
        lbl = " - " + strip_tags(self.txt)
        return lbl[0:50]
