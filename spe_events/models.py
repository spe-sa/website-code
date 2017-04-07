from django.db import models
from django.conf import settings

from cms.models import CMSPlugin
from cms.models import Page
from cms.models.fields import PageField
from django.db.models.fields import CharField

from mainsite.models import Tier1Discipline


class LowerCaseCharField(CharField):
    """
    Defines a charfield which automatically converts all inputs to
    lowercase and saves.
    """

    def pre_save(self, model_instance, add):
        """
        Converts the string to lowercase before saving.
        """
        current_value = getattr(model_instance, self.attname)
        setattr(model_instance, self.attname, current_value.lower())
        return getattr(model_instance, self.attname)

class UpperCaseCharField(CharField):
    """
    Defines a charfield which automatically converts all inputs to
    lowercase and saves.
    """

    def pre_save(self, model_instance, add):
        """
        Converts the string to lowercase before saving.
        """
        current_value = getattr(model_instance, self.attname)
        setattr(model_instance, self.attname, current_value.upper())
        return getattr(model_instance, self.attname)


class EventMenuModel(models.Model):
    # defines a menu
    #
    event_code = UpperCaseCharField(max_length=25, null=True, help_text='Ex: 17ATCE', )
    heading = models.CharField(max_length=50, null=True, help_text='Ex: About', )
    label = models.CharField(max_length=100, null=True, help_text='Ex: About the Workshop',)
    page_url = PageField(
        verbose_name='Page URL', blank=True, null=True,
        on_delete=models.SET_NULL,
        help_text='A page has priority over an external URL')
    external_url = models.URLField(
        'External URL', blank=True,
        max_length=255,
        help_text='e.g. http://www.spe.org/membership/thank-you')
    menu_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return self.event_code + ": " + self.label

    class Meta:
        verbose_name = "Event Menu"
        ordering = ['menu_order', 'event_code', 'label']

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
                if url.find(replace_host) > -1:
                    url = url.replace(replace_host, new_host)
        return url


class EventMenuPluginModel(CMSPlugin):
    # allows user to add an event menu to their page (pulls all event menu items for a meeting code)
    event_code = models.CharField(max_length=25, null=True, help_text='Ex: 17ATCE', )

    def __unicode__(self):
        if self.event_code:
            return self.event_code
        else:
            return ""


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
