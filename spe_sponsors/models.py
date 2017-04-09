from django.db import models
from adminsortable.fields import SortableForeignKey
from adminsortable.models import SortableMixin


class Event(models.Model):
    class Meta:
        verbose_name_plural = 'Event'

    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title


class SponsorCategory(SortableMixin):
    class Meta:
        ordering = ['category_order']
        verbose_name_plural = 'Sponsorship Categories'

    event = SortableForeignKey(Event)
    title = models.CharField(max_length=50)

    # ordering field
    category_order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __unicode__(self):
        return self.title


class Sponsor(models.Model):
    class Meta:
        verbose_name_plural = 'Sponsor'

    title = models.CharField(max_length=50)

    def __unicode__(self):
        return self.title