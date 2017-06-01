from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField
from colorfield.fields import ColorField
from filer.fields.image import FilerImageField
from cms.models.fields import PageField

from django.utils.translation import ugettext_lazy as _

DEFAULT_TYPE = 'tabs/tabheader.html'
TYPES = (
    (DEFAULT_TYPE, 'Tabs'),
    ('tabs/accordionheader.html', 'Accordion'),
)

DEFAULT_SPACER_WIDTH = 'col-xs-12'
SPACER_WIDTH = (
    (DEFAULT_SPACER_WIDTH, '12 Cols'),
    ('col-xs-11', '11 Cols'),
    ('col-xs-10', '10 Cols'),
    ('col-xs-9', '9 Cols'),
    ('col-xs-8', '8 Cols'),
    ('col-xs-7', '7 Cols'),
    ('col-xs-6', '6 Cols'),
    ('col-xs-5', '5 Cols'),
    ('col-xs-4', '4 Cols'),
    ('col-xs-3', '3 Cols'),
    ('col-xs-2', '2 Cols'),
    ('col-xs-1', '1 Col'),
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
    name = models.CharField(max_length=64, blank=True, null=True)
    heading = models.CharField(max_length=64, blank=True, null=True, )
    footer = models.CharField(max_length=64, blank=True, null=True, )
    custom_class = models.CharField(max_length=64, blank=True, null=True, default='panel-default')

    def __unicode__(self):
        return u"{0}".format(self.name)


class TabHeader(CMSPlugin):
    """
    A plugin that has Tab classes as children.
    """
    name = models.CharField(max_length=64, blank=True, null=True)
    type = models.CharField(max_length=255, choices=TYPES, default=DEFAULT_TYPE)

    def __unicode__(self):
        dictionary = dict(TYPES)
        return u"{0} - {1} - {2} tabs".format(self.name, dictionary[self.type], self.cmsplugin_set.all().count())


class Tab(CMSPlugin):
    """
    An individual Tab for the TabHeader plugin.
    """
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u"{0}".format(self.title)


class SpacerPlug(CMSPlugin):
    name = models.CharField('Name', unique=False, max_length=100, blank=True, null=True)
    width = models.CharField(max_length=10, choices=SPACER_WIDTH, default=DEFAULT_SPACER_WIDTH, verbose_name=u'Width '
                                                                                                             u'in '
                                                                                                             u'Boot'
                                                                                                             u'strap '
                                                                                                             u'Colu'
                                                                                                             u'mns.', )
    height = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'Height in pixels.', )

    def __unicode__(self):
        return u"Spacer Plug: {0} width: {1}px height".format(self.width, self.height)


class SingleLinkPlug(CMSPlugin):
    text = models.CharField('Text', unique=False, max_length=100, blank=True, null=True)
    iconurl = models.CharField(max_length=500, null=True, blank=True, help_text=_('URL of external icon, overides '
                                                                                  'Django Filer Image if provided'))
    iconimage = FilerImageField(blank=True, null=True, verbose_name=u'Image for This Icon',
                                related_name="icon_image")
    external_link = models.URLField(
        verbose_name=_('External link'),
        blank=True,
        max_length=2040,
        help_text=_('Provide a valid URL to an external website.'),
    )
    internal_link = PageField(
        verbose_name=_('Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )
    fontawesome = models.CharField('FontAwesome Icon', unique=False, max_length=100, blank=True, null=True)
    isbutton = models.BooleanField(default=False, verbose_name="Is this a button?")
    isinbox = models.BooleanField(default=False, verbose_name="Is this link in a box?")
    height = models.CharField(verbose_name=u'Box height in pixels.', unique=False, max_length=10, blank=True, null=True)
    width = models.CharField(max_length=10, choices=SPACER_WIDTH, default=DEFAULT_SPACER_WIDTH,
                             verbose_name=u'Width n Bootstrap Columns.', )
    bkg_color = ColorField(verbose_name='Background Color', default="#cccccc")
    txt_color = ColorField(verbose_name='Text Color', default="#000000")
    new_window = models.BooleanField(verbose_name=_('Open in new window'), default=False)

    def get_icon_url(self):
        icon = "#"
        if self.imageurl:
            icon = self.iconurl
        elif self.image:
            icon = self.iconimage.url
        return icon

    def get_absolute_url(self):
        link = "#"
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        return link

    def __unicode__(self):
        return u"Link: {0}".format(self.text)
