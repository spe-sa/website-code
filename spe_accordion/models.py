from django.db import models
from cms.models import CMSPlugin


class AccordionHeader(CMSPlugin):
    """
    A plugin that has Tab classes as children.
    """

    def __unicode__(self):
        return u"{0} accordions".format(self.cmsplugin_set.all().count())


class Accordion(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)
