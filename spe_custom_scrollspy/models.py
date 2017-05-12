from django.db import models
from cms.models import CMSPlugin

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin


class ScrollSpyHeader(CMSPlugin):
    """
    A plugin that has Carousel classes as children.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0} - {1} scrollspy items".format(self.title, self.cmsplugin_set.all().count())


class ScrollSpy(CMSPlugin):
    """
    An individual Carousel for the CarouselHeader plugin.
    """
    title = models.CharField(max_length=64)

    def __unicode__(self):
        return u"{0}".format(self.title)



