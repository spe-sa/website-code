# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

# from .models import Promotion, SimpleEventPromotion
from .models import SimpleEventPromotion


# admin.site.register(Promotion)
admin.site.register(SimpleEventPromotion)
