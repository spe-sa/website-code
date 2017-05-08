from django.contrib.gis.geoip import GeoIP
from tastypie.resources import ModelResource
from tastypie.authorization import Authorization
from .models import MembershipPromotionsClicks, PromotionsEventClicks, SimpleEventPromotion


class MembershipPromotionsClicksResource(ModelResource):
    class Meta:
        queryset = MembershipPromotionsClicks.objects.all()
        resource_name = 'membership'
        # authorization = Authorization()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        g = GeoIP()
        bundle.data['Country'] = g.country(bundle.data['ip'])
        return bundle


class PromotionsEventClicksResource(ModelResource):
    class Meta:
        queryset = PromotionsEventClicks.objects.all()
        resource_name = 'promotions'
        # authorization = Authorization()
        allowed_methods = ['get']

    def dehydrate(self, bundle):
        g = GeoIP()
        bundle.data['Country'] = g.country(bundle.data['ip'])
        return bundle


class SimpleEventPromotionResource(ModelResource):
    class Meta:
        queryset = SimpleEventPromotion.objects.all()
        resource_name = 'event_promotion'
        # authorization = Authorization()
        allowed_methods = ['get']

