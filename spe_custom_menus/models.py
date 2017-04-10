from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField

from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin

from django.utils.translation import ugettext_lazy as _


LEVEL_CHOICES = ((1, "Top Level"),
                 (2, "Dropdown Level"),
                )


class CustomMenus(models.Model):
    title = models.CharField('Title', null=True, blank=True, max_length=100)
    branding = models.CharField('Branding on menu', null=True, blank=True, max_length=30)
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
    custom_menu = models.ForeignKey(CustomMenus)

    def __unicode__(self):
        return u"{0}".format(self.custom_menu)

