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


class CustomColumn(CMSPlugin):
    name = models.CharField('Name', unique=False, max_length=100, blank=True, null=True)
    device_count_range = (
        ('0', 'Not Set',),
        ('1', '1/12',),
        ('2', '2/12',),
        ('3', '3/12',),
        ('4', '4/12',),
        ('5', '5/12',),
        ('6', '6/12',),
        ('7', '7/12',),
        ('8', '8/12',),
        ('9', '9/12',),
        ('10', '10/12',),
        ('11', '11/12',),
        ('12', '12/12',),
    )

    bkg_color = ColorField(verbose_name='Background Color')
    transparent = models.BooleanField(default=True, help_text='Transparent overrides selected color')
    mobile_device_width = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           help_text="""The column width on
                                           mobile devices (> 768px)""")
    small_device_width = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          help_text="""The column width on
                                          small (tablet) devices (768px - 992px
                                          )""")
    medium_device_width = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           help_text="""The column width on
                                           medium (small screen
                                           computers/laptops) devices (992px -
                                           1200px) """)
    large_device_width = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          help_text="""The column width on
                                          large devices (1200px and over)""")
    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")
    element_class = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""classes to be applied to this
                                     element""", verbose_name="Element classes"
                                     )
    hide_on_mobile = models.BooleanField(help_text="""If selected, this
                                                 item will not display on
                                                 mobile devices (> 768px)""")
    hide_on_small = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on small devices (768px -
                                                  992px)""")
    hide_on_medium = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on medium devices (992px -
                                                  1200px)""")
    hide_on_large = models.BooleanField(help_text="""If selected,
                                                  this item will not display
                                                  on large devices (1200px and
                                                  over)""")
    mobile_device_offset = models.CharField(max_length=255,
                                            choices=device_count_range,
                                            blank=True,
                                            help_text="""The column offset on
                                            mobile devices (> 768px)""")
    small_device_offset = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           blank=True,
                                           help_text="""The column offset on
                                           small (tablet) devices (768px -
                                           992px)""")

    medium_device_offset = models.CharField(max_length=255,
                                            choices=device_count_range,
                                            blank=True,
                                            help_text="""The column offset on
                                            medium (small screen
                                            computers/laptops) devices (992px -
                                            1200px) """)
    large_device_offset = models.CharField(max_length=255,
                                           choices=device_count_range,
                                           blank=True,
                                           help_text="""The column offset on
                                           large devices (1200px and over)""")
    mobile_device_pull = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column pull on
                                          mobile devices (> 768px)""")
    small_device_pull = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column pull on
                                         small (tablet) devices (768px - 992px
                                         )""")
    medium_device_pull = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column pull on
                                          medium (small screen
                                          computers/laptops) devices (992px -
                                          1200px) """)
    large_device_pull = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column pull on
                                         large devices (1200px and over)""")

    mobile_device_push = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column push on
                                          mobile devices (> 768px)""")
    small_device_push = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column push on
                                         small (tablet) devices (768px - 992px
                                         )""")
    medium_device_push = models.CharField(max_length=255,
                                          choices=device_count_range,
                                          blank=True,
                                          help_text="""The column push on
                                          medium (small screen
                                          computers/laptops) devices (992px -
                                          1200px) """)
    large_device_push = models.CharField(max_length=255,
                                         choices=device_count_range,
                                         blank=True,
                                         help_text="""The column push on
                                         large devices (1200px and over)""")

    content = PlaceholderField('column_placeholder')

    def __unicode__(self):
        return u"Column with {0} items".format(self.cmsplugin_set.all().count())

    @property
    def get_mobile_width(self):
        if self.mobile_device_width != 0:
            return "col-xs-%s" % self.mobile_device_width

    @property
    def get_small_width(self):
        if self.small_device_width != 0:
            return "col-sm-%s" % self.small_device_width

    @property
    def get_medium_width(self):
        if self.medium_device_width != 0:
            return "col-md-%s" % self.medium_device_width

    @property
    def get_large_width(self):
        if self.large_device_width != 0:
            return "col-lg-%s" % self.large_device_width

    @property
    def get_mobile_offset(self):
        if self.mobile_device_offset != 0:
            return "col-xs-offset-%s" % self.mobile_device_offset

    @property
    def get_small_offset(self):
        if self.small_device_offset != 0:
            return "col-sm-offset-%s" % self.small_device_offset

    @property
    def get_medium_offset(self):
        if self.medium_device_offset != 0:
            return "col-md-offset-%s" % self.medium_device_offset

    @property
    def get_large_offset(self):
        if self.large_device_offset != 0:
            return "col-lg-offset-%s" % self.large_device_offset

    @property
    def get_mobile_pull(self):
        if self.mobile_device_pull != 0:
            return "col-xs-pull-%s" % self.mobile_device_pull

    @property
    def get_small_pull(self):
        if self.small_device_pull != 0:
            return "col-sm-pull-%s" % self.small_device_pull

    @property
    def get_medium_pull(self):
        if self.medium_device_pull != 0:
            return "col-md-pull-%s" % self.medium_device_pull

    @property
    def get_large_pull(self):
        if self.large_device_pull != 0:
            return "col-lg-pull-%s" % self.large_device_pull

    @property
    def get_mobile_push(self):
        if self.mobile_device_push != 0:
            return "col-xs-push-%s" % self.mobile_device_push

    @property
    def get_small_push(self):
        if self.small_device_push != 0:
            return "col-sm-push-%s" % self.small_device_push

    @property
    def get_medium_push(self):
        if self.medium_device_push != 0:
            return "col-md-push-%s" % self.medium_device_push

    @property
    def get_large_push(self):
        if self.large_device_push != 0:
            return "col-lg-push-%s" % self.large_device_push

    @property
    def is_hidden_on_mobile(self):
        if self.hide_on_mobile:
            return "hidden-xs"

    @property
    def is_hidden_on_small(self):
        if self.hide_on_small:
            return "hidden-sm"

    @property
    def is_hidden_on_medium(self):
        if self.hide_on_medium:
            return "hidden-md"

    @property
    def is_hidden_on_large(self):
        if self.hide_on_large:
            return "hidden-lg"

    @property
    def get_column_widths(self):
        return "%s %s %s %s" % (self.get_mobile_width,
                                self.get_small_width,
                                self.get_medium_width,
                                self.get_large_width)

    @property
    def get_column_pulls(self):
        return "%s %s %s %s" % (self.get_mobile_pull,
                                self.get_small_pull,
                                self.get_medium_pull,
                                self.get_large_pull)

    @property
    def get_column_pushes(self):
        return "%s %s %s %s" % (self.get_mobile_push,
                                self.get_small_push,
                                self.get_medium_push,
                                self.get_large_push)

    @property
    def get_column_offsets(self):
        return "%s %s %s %s" % (self.get_mobile_offset,
                                self.get_small_offset,
                                self.get_medium_offset,
                                self.get_large_offset)

    @property
    def get_column_classes(self):
        return "%s %s %s %s %s" % (self.get_column_widths,
                                   self.get_column_pulls,
                                   self.get_column_pushes,
                                   self.get_column_offsets,
                                   self.element_class)


class CustomRow(CMSPlugin):
    name = models.CharField('Name', unique=False, max_length=100, blank=True, null=True)
    bkg_color = ColorField(verbose_name='Background Color')
    transparent = models.BooleanField(default=True, help_text='Transparent overrides selected color')
    classes = models.CharField(max_length=255, null=True, blank=True,
                               help_text="""Classes to be applied to this
                               element""", verbose_name="Element Classes")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")

    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")

    def __unicode__(self):
        return u"Row with {0} items :: {1}".format(self.cmsplugin_set.all().count(), self.name)


class Container(CMSPlugin):
    name = models.CharField('Name', unique=False, max_length=100, blank=True, null=True)
    bkg_color = ColorField(verbose_name='Background Color')
    transparent = models.BooleanField(default=True, help_text='Transparent overrides selected color')
    classes = models.CharField(max_length=255, null=True, blank=True,
                               help_text="""Classes to be applied to this
                               element""", verbose_name="Element Classes")
    element_id = models.CharField(max_length=255, null=True, blank=True,
                                  help_text="""ID's to be applied to this
                                  element""", verbose_name="Element ID's")

    element_style = models.CharField(max_length=255, null=True, blank=True,
                                     help_text="""HTML styles to be applied to
                                     this element""",
                                     verbose_name="Element style")
    is_fluid = models.BooleanField(default=True)

    def __unicode__(self):
        return u"Container with {0} items :: {1}".format(self.cmsplugin_set.all().count(), self.name)

    @property
    def get_is_fluid(self):
        print self.is_fluid
        if self.is_fluid is True:
            return "container-fluid"
        else:
            return "container"


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
    width = models.CharField(max_length=10, choices=SPACER_WIDTH, default=DEFAULT_SPACER_WIDTH, verbose_name=u'Width n Bootstrap Columns.', )
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
