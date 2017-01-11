from django.contrib.gis.geoip import GeoIP
from mainsite.models import Web_Region_Country
from mainsite.context_processors.spe_context import get_ip


def getRegion(context, fallback_region):
    g = GeoIP()
    # ip = context['request'].META.get('REMOTE_ADDR', None)
    # ip = context['request'].META.get('HTTP_X_REAL_IP', None)
    ip = get_ip(context['request'])
    region = fallback_region
    if ip:
        loc = g.city(ip)
        if loc:
            country = loc['country_code3']
            try:
                region = Web_Region_Country.objects.get(country_UN=country).region
            except Web_Region_Country.DoesNotExist:
                region = Web_Region_Country.objects.get(country_UN=fallback_region).region
    return region