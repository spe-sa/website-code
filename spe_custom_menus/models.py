from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin

from django.utils.translation import ugettext_lazy as _

DEFAULT_MENU_TEMPLATE = 'spe_custom_menus/bootstrap_menu.html'
MENU_TEMPLATES = (
    (DEFAULT_MENU_TEMPLATE, 'Bootstrap Menu'),
    ('spe_custom_menus/YAMM_menu.html', 'YAMM Menu'),
)

LEVEL_CHOICES = ((1, "Top Level"),
                 (2, "Dropdown Level"),
                 (3, "Dropdown Header"),
                 (4, "Divider"),
                 )


class CustomMenus(models.Model):
    title = models.CharField('Menu name', unique=True, max_length=100)
    branding = models.CharField('Branding on menu', null=True, blank=True, max_length=30)
    external_link = models.URLField(
        verbose_name=_('Brand External link'),
        blank=True,
        max_length=2040,
        help_text=_('Provide a valid URL to an external website.'),
    )
    internal_link = PageField(
        verbose_name=_('Brand Internal link'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )

    class Meta:
        verbose_name_plural = 'Custom Menus'

    def get_absolute_url(self):
        link = "#"
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        return link

    def __unicode__(self):
        return self.title


class CustomMenuItems(SortableMixin):
    custom_menu = SortableForeignKey(CustomMenus, verbose_name='Custom Menu')
    title = models.CharField('Title', null=True, blank=True, max_length=50)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
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
    is_dropdown_node = models.BooleanField(default=False, editable=False)
    is_back_up = models.BooleanField(default=False, editable=False)
    is_dropdown_header = models.BooleanField(default=False, editable=False)
    is_divider = models.BooleanField(default=False, editable=False)

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Custom Menu Items'

    # ordering field
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def get_link(self):
        link = "#"
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        return link

    def __unicode__(self):
        dictionary = dict(LEVEL_CHOICES)
        return dictionary[self.level] + " - " + self.title


class CustomMenusPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=MENU_TEMPLATES, default=DEFAULT_MENU_TEMPLATE)
    custom_menu = models.ForeignKey(CustomMenus,
                                    help_text="Select a menu you created in Admin or use '+' to add a new menu")

    def __unicode__(self):
        dictionary = dict(MENU_TEMPLATES)
        return u"{0} using {1}".format(self.custom_menu, dictionary[self.template])
