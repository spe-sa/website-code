from django.db import models
from cms.models import CMSPlugin


class Panel(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=64)
    heading = models.CharField(max_length=64, blank=True, null=True,)
    footer = models.CharField(max_length=64, blank=True, null=True,)
    custom_class = models.CharField(max_length=64, blank=True, null=True, default='panel-default')


    def __unicode__(self):
        return u"{0}".format(self.title)
