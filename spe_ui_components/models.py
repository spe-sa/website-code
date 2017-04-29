from django.db import models
from cms.models import CMSPlugin

DEFAULT_TYPE = 'tabs/tabheader.html'
TYPES = (
    (DEFAULT_TYPE, 'Tabs'),
    ('tabs/accordionheader.html', 'Accordion'),
)


class CarouselHeader(CMSPlugin):
    """
    A plugin that has Carousel classes as children.
    """

    def __unicode__(self):
        return u"{0} carousel items".format(self.cmsplugin_set.all().count())


class Carousel(CMSPlugin):
    """
    An individual Carousel for the CarouselHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)


class Jumbotron(CMSPlugin):
    """
     An individual Jumbotron plugin.
    """

    def __unicode__(self):
        return u"Jumbotron"


class Panel(CMSPlugin):
    """
    An individual Panel plugin.
    """
    title = models.CharField(max_length=64)
    heading = models.CharField(max_length=64, blank=True, null=True,)
    footer = models.CharField(max_length=64, blank=True, null=True,)
    custom_class = models.CharField(max_length=64, blank=True, null=True, default='panel-default')


    def __unicode__(self):
        return u"{0}".format(self.title)


class TabHeader(CMSPlugin):
    """
    A plugin that has Tab classes as children.
    """
    type = models.CharField(max_length=255, choices=TYPES, default=DEFAULT_TYPE)

    def __unicode__(self):
        dictionary = dict(TYPES)
        return u"{0} - {1} tabs".format(dictionary[self.type], self.cmsplugin_set.all().count())


class Tab(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)
