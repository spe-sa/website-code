# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _

from cms.plugin_pool import plugin_pool

from .segment_plugin_base import SegmentPluginBase

from django.contrib.gis.geoip import GeoIP

from ..models import (
    AuthenticatedSegmentPluginModel,
    CookieSegmentPluginModel,
    FallbackSegmentPluginModel,
    SwitchSegmentPluginModel,
    DisciplineSegmentPluginModel,
    CountrySegmentPluginModel,
)


class FallbackSegmentPlugin(SegmentPluginBase):
    '''
    This segment plugin represents a degenerate case where the segment
    always matches.
    '''

    model = FallbackSegmentPluginModel
    name = _('Fallback')

    # It doesn't make much sense to override this one...
    allow_overrides = False

    def is_context_appropriate(self, context, instance):
        return True


class SwitchSegmentPlugin(SegmentPluginBase):
    '''
    This switch segmentation plugin allows the operator to turn the segment ON
    or OFF statically and independently from the context. This is primarily
    useful for testing.
    '''

    model = SwitchSegmentPluginModel
    name = _('Segment by switch')

    # It doesn't make much sense to override this one...
    allow_overrides = False

    def is_context_appropriate(self, context, instance):
        return instance.on_off


class CookieSegmentPlugin(SegmentPluginBase):
    '''
    This is a segmentation plugin that renders output on the condition that a
    cookie with ``cookie_key`` is present and has the value ``cookie_value``.
    '''

    model = CookieSegmentPluginModel
    name = _('Segment by cookie')

    def is_context_appropriate(self, context, instance):
        request = context.get('request')
        value = request.COOKIES.get(instance.cookie_key)
        return (value == instance.cookie_value)


class AuthenticatedSegmentPlugin(SegmentPluginBase):
    '''
    This plugin allows segmentation based on the authentication/authorization
    status of the visitor.
    '''

    model = AuthenticatedSegmentPluginModel
    name = _('Segment by auth')

    def is_context_appropriate(self, context, instance):
        request = context.get('request')
        return request and request.user and request.user.is_authenticated()

class DisciplineSegmentPlugin(SegmentPluginBase):
    '''
    This plugin allows segmentation based on the discipline of the visitor.
    '''

    model = DisciplineSegmentPluginModel
    name = _('Segment by discipline')

    def is_context_appropriate(self, context, instance):
        request = context.get('request')
        value = request.COOKIES.get("discipline")
        return (value == instance.discipline)

class CountrySegmentPlugin(SegmentPluginBase):
    '''
    This plugin allows segmentation based on the visitor's IP addresses
    associated country code. Use of this segment requires the use of the
    'resolve_country_code_middleware' provided in this distribution. This
    middleware, in turn, depends on django.contrib.geo_ip and MaxMind's
    GeoLite dataset or similar.
    '''

    model = CountrySegmentPluginModel
    name = _('Segment by country')

    #
    # If django-easy-select2 is installed, we can greatly enhance the
    # useability of this change form.
    #
    try:
        from easy_select2 import select2_modelform
        form = select2_modelform(CountrySegmentPluginModel, attrs={'width': '250px'})
    except:
        pass

    def is_context_appropriate(self, context, instance):
        g = GeoIP()
        request = context.get('request')
        user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')[:400]
        # ip_address in case I need to take proxies into account
        ip_address = (
            request.META.get('HTTP_X_FORWARDED_FOR')
            if 'HTTP_X_FORWARDED_FOR' in request.META
            else request.META.get('REMOTE_ADDR')
        )[:100]
        ip = request.META.get('REMOTE_ADDR', None) 
        if ip:
            code = g.country(ip)['country_code']
        else:
            code = 'XB'
        return (code == instance.country_code)

plugin_pool.register_plugin(AuthenticatedSegmentPlugin)
plugin_pool.register_plugin(CookieSegmentPlugin)
plugin_pool.register_plugin(FallbackSegmentPlugin)
plugin_pool.register_plugin(DisciplineSegmentPlugin)
plugin_pool.register_plugin(CountrySegmentPlugin)
plugin_pool.register_plugin(SwitchSegmentPlugin)
