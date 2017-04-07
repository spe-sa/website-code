from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField

from django.utils.translation import ugettext_lazy as _


LEVEL_CHOICES = ((1, "Top Level Item without Dropdown"),
                 (2, "Top Level Item with Dropdown"),
                 (3, "Dropdown Item"))

class MenuItem(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=255)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    url = PageField(verbose_name="Page to link to", blank=True, null=True, on_delete=models.SET_NULL)
    sequence = models.PositiveIntegerField(default=0, editable=False)
    transition = models.PositiveIntegerField(default=0, editable=False)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    class Meta(object):
        ordering = ('my_order',)

    def __unicode__(self):
        dictionary = dict(LEVEL_CHOICES)
        return dictionary[self.level] + " - " + self.title


class Menu(CMSPlugin):
    event = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.event)