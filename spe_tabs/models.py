from django.db import models
from cms.models import CMSPlugin

DEFAULT_TYPE = 'spe_tabs/tabheader.html'
TYPES = (
    (DEFAULT_TYPE, 'Tabs'),
    ('spe_tabs/accordionheader.html', 'Accordion'),
)


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
