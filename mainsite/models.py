from django.db import models
# from django.core.urlresolvers import reverse
# from django.utils import six
# from django.utils.encoding import python_2_unicode_compatible, force_text
# from django.utils.functional import lazy
# from django.utils.translation import ugettext_lazy as _, string_concat

from cms.models import CMSPlugin

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
#)

#class PageTemplate(models.Model):
#    type_of_page = models.CharField(max_length=255, choices=PAGE_TYPES, default=DEFAULT_PAGE_TYPE)
#    template = models.CharField(max_length=255, choices=PAGE_TEMPLATES, default=DEFAULT_PAGE_TEMPLATE)


class Tier1Discipline(models.Model):
    number = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=3, primary_key=True)
    long_code = models.CharField(max_length=20, blank=True, null=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


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
