from django.db import models
from django.core.urlresolvers import reverse
from django.utils import six
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import lazy
from django.utils.translation import ugettext_lazy as _, string_concat

from cms.models import CMSPlugin

class Discipline(models.Model):
    number = models.CharField(max_length=12, unique=True)
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=150)
    active = models.BooleanField(default=True)

    def __str__(self):
        return  self.name

    class Meta:
        ordering = ['name']

class AdSpeedZoneAdPluginModel(CMSPlugin):
    name = models.CharField(
        max_length = 255,
        verbose_name="Advertising Block Name",
    )
    div_id = models.CharField(
        max_length = 100,
        verbose_name="div id for ad",
        blank=True,
        null=True,
    )
    div_class = models.CharField(
        max_length = 100,
        verbose_name="div class for ad",
        blank=True,
        null=True,
    )
    zid = models.PositiveIntegerField(
        verbose_name="Zone id",
    )

    def __unicode__(self):
        return self.name

