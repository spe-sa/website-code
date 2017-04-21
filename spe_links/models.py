# -*- coding: utf-8 -*-
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin

from django.utils.translation import ugettext_lazy as _

# import datetime
from cms.models import CMSPlugin
from cms.models import Page
from cms.models.fields import PageField
from django.db import models
# from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.conf import settings

class PageLinkSet(models.Model):
    title = models.CharField('Title', max_length=100, unique=True)
    show_all_text = models.CharField(max_length=50, blank=True, null=True)
    show_all_internal_link = PageField(
        verbose_name=_('Internal Page'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )
    show_all_external_link = models.URLField(
        verbose_name=_('External Link'),
        blank=True,
        max_length=2040,
        help_text=_('Provide a valid URL to an external website.'),
    )

    class Meta:
        verbose_name_plural = 'Set of Links'

    def get_absolute_url(self):
        link = ""
        if self.show_all_internal_link:
            link = self.show_all_internal_link.get_absolute_url()
        elif self.show_all_external_link:
            link = self.show_all_external_link
        return link

    def __unicode__(self):
        return self.title

class PageLink(SortableMixin):
    page_set = SortableForeignKey(PageLinkSet)
    title = models.CharField(max_length=255)

    internal_page = PageField(
        verbose_name=_('Internal page'),
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text=_('If provided, overrides the external link.'),
    )
    external_page = models.URLField(
        verbose_name=_('External url'),
        blank=True,
        max_length=2040,
        help_text=_('Provide a valid URL to an external website.'),
    )

    class Meta:
        ordering = ['order']
        verbose_name_plural = 'Set of Links'

    # ordering field
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def get_absolute_url(self):
        link = "#"
        if self.internal_page:
            link = self.internal_page.get_absolute_url()
        elif self.external_page:
            link = self.external_page
        return link

    def __unicode__(self):
        return self.title

class PageLinkSetPlugin(CMSPlugin):
    link_set = models.ForeignKey(PageLinkSet, on_delete=models.SET_NULL, null=True)
    additional_classes = models.CharField(max_length=255, blank=True, null=True, help_text=_('class names delimited by spaces that will be appended'))

    def __unicode__(self):
        return self.link_set.title


@python_2_unicode_compatible  # only if you need to support Python 2
class SpeLinkCategory(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    # Adding class name; if present will be used instead of the name lower case
    class_name = models.CharField(max_length=255, blank=True, null=True)
    # Adding category url if present will show all link to the url location
    show_all_page = PageField(
        verbose_name=_('Show all - Page URL'), blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text=_('A page has priority over an external URL'))
    show_all_external = models.URLField(
        _('Show all - External URL'), blank=True,
        max_length=255,
        help_text=_('e.g. http://www.spe.org/membership/thank-you'))

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def get_absolute_url(self):
        if self.show_all_page:
            page = Page.objects.get(pk=self.show_all_page.id)
            url = page.get_absolute_url()
        else:
            url = self.show_all_external
        # TODO: push this down to the SPEURLFIELD level and replace the URLFields above
        # replace all instances containing '//production_host_name/' with //env.hostname/ if we have env.hostname
            replacements = getattr(settings, "HOST_REPLACEMENTS", None)
        if replacements:
            for replace_host, new_host in replacements:
                if (url.find(replace_host) > -1):
                    url = url.replace(replace_host, new_host)
        return url


@python_2_unicode_compatible  # only if you need to support Python 2
class SpeLink(models.Model):
    category = models.ForeignKey(SpeLinkCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255, null=True)
    page_url = PageField(
        verbose_name=_('Page URL'), blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text=_('A page has priority over an external URL'))
    external_url = models.URLField(
        _('External URL'), blank=True,
        max_length=255,
        help_text=_('e.g. http://www.spe.org/membership/thank-you'))

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name = "link"
        ordering = ['category__title', 'title']

    def get_absolute_url(self):
        if self.page_url:
            page = Page.objects.get(pk=self.page_url.id)
            url = page.get_absolute_url()
        else:
            url = self.external_url
        # TODO: push this down to the SPEURLFIELD level and replace the URLFields above
        # replace all instances containing '//production_host_name/' with //env.hostname/ if we have env.hostname
        replacements = getattr(settings, "HOST_REPLACEMENTS", None)
        if replacements:
            for replace_host, new_host in replacements:
                if (url.find(replace_host) > -1):
                    url = url.replace(replace_host, new_host)
        return url


@python_2_unicode_compatible
class SpeLinkPluginModel(CMSPlugin):
    category = models.ForeignKey(SpeLinkCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.category.title
