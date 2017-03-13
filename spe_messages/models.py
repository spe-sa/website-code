# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.utils.translation import ugettext_lazy as _, string_concat

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from cms.models import CMSPlugin
from filer.fields.image import FilerImageField
from ckeditor_uploader.fields import RichTextUploadingField

from mainsite.models import Customer, CustomerClassification


DEFAULT_MESSAGE_PLUGIN_TEMPLATE = 'spe_messages/plugins/promotion_posts.html'
MESSAGE_PLUGIN_TEMPLATES = (
    (DEFAULT_MESSAGE_PLUGIN_TEMPLATE, 'Listing'),
)


class TargetedMessage(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    message = models.CharField(
        max_length=300,
    )
    show_start_date = models.DateTimeField()
    show_end_date = models.DateTimeField()
    show_to = models.ManyToManyField(CustomerClassification, blank=True, db_constraint=False)

    class Meta:
        verbose_name = 'Targeted Message'

    def __unicode__(self):
        return self.title

    def copy_relations(self, old_instance):
        self.classifications = old_instance.classifications.all()



class TargetedMessageForMemberPlugin(CMSPlugin):
    template = models.CharField(max_length=255, choices=MESSAGE_PLUGIN_TEMPLATES,
                                default=DEFAULT_MESSAGE_PLUGIN_TEMPLATE)
    count = models.PositiveIntegerField(default=5, verbose_name=u'Number of Messages to Show')
    classifications = models.ManyToManyField(CustomerClassification, blank=True, db_constraint=False)

    def __unicode__(self):
        dictionary = dict(MESSAGE_PLUGIN_TEMPLATES)
        buf = dictionary[self.template] + " - " + str(self.count) + " - "
        buf += "%s, " % ', '.join([a.description for a in self.classifications.all()])
        return buf

    def copy_relations(self, old_instance):
        self.classifications = old_instance.classifications.all()
