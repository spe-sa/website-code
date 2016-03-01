import datetime
from cms.models import CMSPlugin
from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible  # only if you need to support Python 2
class SpeLinkCategory(models.Model):
    code = models.CharField(max_length=20)
    title = models.CharField(max_length=255)
    # Adding class name; if present will be used instead of the name lower case
    class_name = models.CharField(max_length=255, blank=True, null=True)
    # Adding category url if present will show all link to the url location
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name = "category"


@python_2_unicode_compatible  # only if you need to support Python 2
class SpeLink(models.Model):
    category = models.ForeignKey(SpeLinkCategory, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=255, null=True)
    url = models.URLField(max_length=255, blank=True, null=True)

    def __str__(self):  # __unicode__ on Python 2
        return self.title

    class Meta:
        verbose_name = "link"
        ordering = ['category__title', 'title']


@python_2_unicode_compatible
class SpeLinkPluginModel(CMSPlugin):
    category = models.ForeignKey(SpeLinkCategory)

    def __str__(self):
        return self.category.title
