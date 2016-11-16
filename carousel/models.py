# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from cms.models import CMSPlugin, Model


@python_2_unicode_compatible
class CarouselModel(CMSPlugin):
    #

    label = models.CharField(
        blank=True,
        default='',
        help_text=_('Optionally set a label for this carousel.'),
        max_length=128,
    )

    def __str__(self):
        """
        If there is a label, show that with the configuration in brackets,
        otherwise, just return the configuration string.
        """

        if self.label:
            return self.label
        else:
            return ""


@python_2_unicode_compatible
class CarouselComponentModel(CMSPlugin):
    # defines a component in terms of dates, clicks and impressions
    # hoping to use this to solve our falling off or start problem

    start_display = models.DateField(blank=True, null=True, default=timezone.now)
    stop_display = models.DateField(blank=True, null=True)
    link_to = models.URLField(max_length=128, blank=True, null=True,
                              help_text=_("optional: link to page when carousel item is clicked."))
    is_tracking = models.BooleanField(_("Tracking"), default=True, help_text=_("optional: toggle click through and impression tracking."))

    @property
    def component_href(self):
        if self.is_tracking:
            return "/carousel/clicked/" + str(self.id)
        return "#"

    @property
    def show_component(self):
        """
        Return if this item should be shown based on dates given
        """
        now = timezone.now().date()
        if self.start_display is None and self.stop_display is None:
            return True
        if self.start_display is None or self.start_display <= now:
            if self.stop_display is None:
                return True
            if self.stop_display >= now:
                return True
        return False

    def __str__(self):
        """
        If there is a label, show that with the configuration in brackets,
        otherwise, just return the configuration string.
        """
        buf = ""
        if self.start_display:
            buf += self.start_display.strftime('%d-%b-%Y %H:%M')
        else:
            buf += "Whenever"
        buf += " - "
        if self.stop_display:
            buf += self.stop_display.strftime('%d-%b-%Y %H:%M')
        else:
            buf += "Forever"
        return buf


# NOTE: I am adding these since they are in the requirements, however, I think this might be better done from apache logs
#   which would require
# @python_2_unicode_compatible
# class CarouselClickThroughTracking(Model):
#
#     vid = models.CharField(blank=True, null=True, help_text=_('visitor information cookie value'), max_length=128,)
#     referrer = models.CharField(blank=True, null=True, max_length=1024)
#     ip = models.CharField(blank=True, null=True, max_length=18)
#     date_clicked = models.DateTimeField(editable=False, default=timezone.now)
#
#     def __str__(self):
#         if self.vid:
#             return self.vid + ": " + _(self.date_clicked)
#         else:
#             return _(self.date_clicked)
#
#
# class CarouselImpressionTracking(Model):
#
#     vid = models.CharField(blank=True, null=True, help_text=_('visitor information cookie value'), max_length=128,)
#     referrer = models.CharField(blank=True, null=True, max_length=1024)
#     ip = models.CharField(blank=True, null=True, max_length=18)
#     date_viewed = models.DateTimeField(editable=False, default=timezone.now)
#
#     def __str__(self):
#         if self.vid:
#             return self.vid + ": " + _(self.date_viewed)
#         else:
#             return _(self.date_viewed)
