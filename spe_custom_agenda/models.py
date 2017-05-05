from django.db import models
from cms.models import CMSPlugin
from cms.models.fields import PageField

from django.utils.translation import ugettext_lazy as _


DEFAULT_AGENDA_TEMPLATE = 'cms_plugins/agenda.html'
AGENDA_TEMPLATES = (
    (DEFAULT_AGENDA_TEMPLATE, 'Regular Schedule'),
    ('cms_plugins/accordion_agenda.html', 'Accordion Schedule'),
)


class CustomAgenda(models.Model):
    title = models.CharField('Meeting Title', unique=True, max_length=100)
    # external_link = models.URLField(
    #     verbose_name=_('External link'),
    #     blank=True,
    #     max_length=2040,
    #     help_text=_('Provide a valid URL to an external website.'),
    # )
    # internal_link = PageField(
    #     verbose_name=_('Internal link'),
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     help_text=_('If provided, overrides the external link.'),
    # )

    class Meta:
        verbose_name = 'Custom Agenda'

    # def get_absolute_url(self):
    #     link = "#"
    #     if self.internal_link:
    #         link = self.internal_link.get_absolute_url()
    #     elif self.external_link:
    #         link = self.external_link
    #     return link

    def __unicode__(self):
        return self.title


class CustomAgendaItems(models.Model):
    custom_agenda = models.ForeignKey(CustomAgenda, verbose_name='Custom Agenda')
    title = models.CharField('Session Title', max_length=80)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # external_link = models.URLField(
    #     verbose_name=_('External link'),
    #     blank=True,
    #     max_length=2040,
    #     help_text=_('Provide a valid URL to an external website.'),
    # )
    # internal_link = PageField(
    #     verbose_name=_('Internal link'),
    #     blank=True,
    #     null=True,
    #     on_delete=models.SET_NULL,
    #     help_text=_('If provided, overrides the external link.'),
    # )
    is_new_day = models.BooleanField(default=False, editable=False)
    rowspan = models.PositiveIntegerField(default=1, editable=False)

    class Meta:
        ordering = ['start_date', 'start_time', 'end_time']
        verbose_name_plural = 'Custom Agenda Items'

    # def get_absolute_url(self):
    #     link = "#"
    #     if self.internal_link:
    #         link = self.internal_link.get_absolute_url()
    #     elif self.external_link:
    #         link = self.external_link
    #     return link

    def __unicode__(self):
        return self.title


class CustomAgendaPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=AGENDA_TEMPLATES, default=DEFAULT_AGENDA_TEMPLATE)
    custom_agenda = models.ForeignKey(CustomAgenda, help_text="Select an agenda you created in Admin or use '+' to add a new agenda")

    def __unicode__(self):
        dictionary = dict(AGENDA_TEMPLATES)
        return u"{0} using {1}".format(self.custom_agenda, dictionary[self.template])

