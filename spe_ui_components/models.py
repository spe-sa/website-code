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


class Modal(CMSPlugin):
    """
    A plugin that has Modal classes as children.
    """
    label = models.CharField('Modal Button Label', max_length=35)

    def __unicode__(self):
        return u"{0} modal items".format(self.cmsplugin_set.all().count())


class ModalBody(CMSPlugin):
    """
    A Modal plugin.
    """


    def __unicode__(self):
        return u"{0} modal body items".format(self.cmsplugin_set.all().count())


class ModalFooter(CMSPlugin):
    """
    A Modal Footer plugin.
    """

    def __unicode__(self):
        return u"{0} - {1} modal footer items".format(self.label, self.cmsplugin_set.all().count())


class ModalHeader(CMSPlugin):
    """
    A Modal Header plugin.
    """

    def __unicode__(self):
        return u"{0} modal header items".format(self.cmsplugin_set.all().count())


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
