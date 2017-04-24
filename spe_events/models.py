from django.db import models
from cms.models import CMSPlugin

from mainsite.models import Tier1Discipline
from mainsite.common import UpperCaseCharField

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
