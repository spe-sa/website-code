from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from django.template.defaultfilters import slugify

from django.utils.translation import ugettext_lazy as _

from mainsite.models import Tier1Discipline
from mainsite.common import UpperCaseCharField

DEFAULT_IMAGE_ITEM_TEMPLATE = 'spe_events/plugins/image_items/ii_boxes.html'
IMAGE_ITEM_TEMPLATES = (
    (DEFAULT_IMAGE_ITEM_TEMPLATE, 'Image Boxes'),
    ('spe_events/plugins/image_items/ii_jumbotron.html', 'Jumbotron'),
    ('spe_events/plugins/image_items/ii_jumboslider.html', 'Jumbo Slider'),
    ('spe_events/plugins/image_items/ii_mini_slider.html', 'Mini Slider'),
    ('spe_events/plugins/image_items/ii_text_below.html', 'Text Below'),
    ('spe_events/plugins/image_items/ii_itemThumb.html', 'Single Image'),
    ('spe_events/plugins/image_items/ii_speakers.html', 'Speakers'),
    ('spe_events/plugins/image_items/ii_video.html', 'Video Item'),
    ('spe_events/plugins/image_items/ii_sponsor_conveyor.html', 'Sponsors - Conveyor'),
    ('spe_events/plugins/image_items/ii_sponsor_panels.html', 'Sponsors - Panels'),
    ('spe_events/plugins/image_items/ii_parallax.html', 'Jumbotron Parallax'),
)

DEFAULT_IMAGE_POSITION = 'center center'
IMAGE_POSITIONS = (
    ('left top', 'Left-Top'),
    ('left center', 'Left-Center'),
    ('left bottom', 'Left-Bottom'),
    ('center top', 'Center-Top'),
    (DEFAULT_IMAGE_POSITION, 'Center-Center'),
    ('center bottom', 'Center-Bottom'),
    ('right top', 'Right-Top'),
    ('right center', 'Right-Center'),
    ('right bottom', 'Right-Bottom'),
)


class EventType(models.Model):
    name = models.CharField(max_length=150, unique=True)
    active = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name


class EventsByCurrentIPPlugin(CMSPlugin):
    number = models.PositiveIntegerField(default=1)
    disciplines = models.ManyToManyField(Tier1Discipline)
    types = models.ManyToManyField(EventType)
    radius = models.PositiveIntegerField(default=500, verbose_name="Radius around location in km")

    def __unicode__(self):
        return "Showing " + str(self.number) + " events"

    def copy_relations(self, old_instance):
        self.disciplines = old_instance.disciplines.all()
        self.types = old_instance.types.all()


class EventSponsors(models.Model):
    eventcode = models.CharField(max_length=150, unique=False)
    sponsorname = models.CharField(max_length=150, unique=False)
    sponsorlink = models.CharField(max_length=150, unique=False)
    sponsorlogo = models.CharField(max_length=150, unique=False)
    sponsororder = models.PositiveIntegerField(unique=True)

    def __unicode__(self):
        return self.sponsorname


class ImageItemList(models.Model):
    title = models.CharField('Title', unique=False, max_length=100)
    event_id = models.CharField('Event ID', null=True, blank=True, max_length=30)

    class Meta:
        verbose_name_plural = 'Image Item List'

    def __unicode__(self):
        return self.title


class ImageItems(SortableMixin):
    item_list = SortableForeignKey(ImageItemList, verbose_name='Item List')
    imageurl = models.CharField(max_length=500, null=True, blank=True, help_text=_('URL to Image, overides Django '
                                                                                   'Filer Image if provided'))
    image = FilerImageField(blank=True, null=True, verbose_name=u'Image for This Item',
                            related_name="item_image")
    imageposition = models.CharField(max_length=255, choices=IMAGE_POSITIONS, default=DEFAULT_IMAGE_POSITION)
    title = models.CharField(max_length=150, unique=False)
    text = RichTextUploadingField(
        max_length=60000,
        help_text=u'Text description of item.',
        blank=True,
        null=True,
    )
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
    new_window = models.BooleanField(verbose_name=_('Open in new window'), default=False)
    isvisible = models.BooleanField(default=True)
    issponsor = models.BooleanField(default=False)
    sponsorlevel = models.CharField(max_length=150, unique=False, null=True, blank=True)
    sponsoredevents = models.CharField(max_length=150, unique=False, null=True, blank=True)
    imgheight = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'Image height in pixels. (not '
                                                                                    u'used everywhere)', )
    imgwidth = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'Image Width in pixels. (not used '
                                                                                   u'everywhere)', )

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Custom Menu Items'

    # ordering field
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def get_image_url(self):
        imagelink = "#"
        if self.imageurl:
            imagelink = self.imageurl
        elif self.image:
            imagelink = self.image.url
        return imagelink

    def get_absolute_url(self):
        link = "#"
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        return link

    def __unicode__(self):
        dictionary = dict(IMAGE_POSITIONS)
        return " - " + self.title + " - "


class ImageItemsPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=IMAGE_ITEM_TEMPLATES, default=DEFAULT_IMAGE_ITEM_TEMPLATE)
    pluginheight = models.CharField(max_length=10, blank=True, null=True, verbose_name=u'Height in pixels.',)
    item_list = models.ForeignKey(ImageItemList,
                                  help_text="Select an image list you created in Admin or use '+' to add a new menu")

    def __unicode__(self):
        dictionary = dict(IMAGE_ITEM_TEMPLATES)
        return u"{0} using {1}".format(self.item_list, dictionary[self.template])


class CalendarEvent(models.Model):
    title = models.CharField('Event title', unique=True, max_length=100)
    slug = models.SlugField(editable=False)
    description = models.CharField('Description', max_length=1000)
    location = models.CharField('Location', max_length=150, blank=True, null=True)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()


    class Meta:
        verbose_name = 'Event Calendar Item'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(CalendarEvent, self).save(*args, **kwargs)

    def __unicode__(self):
        return u"{0} with slug of {1}".format(self.title, self.slug)


class CalendarEventItem(CMSPlugin):
    event = models.ForeignKey(CalendarEvent, help_text="Select event calendar item for iCal export")

    def __unicode__(self):
        return u"{0}".format(self.event.title)