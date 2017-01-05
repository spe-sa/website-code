from django.contrib.gis.geoip import GeoIP
from mainsite.models import Web_Region_Country


def getRegion(context):
    # Use USA as the Default Region Because of Event Volume
    g = GeoIP()
    # ip = context['request'].META.get('REMOTE_ADDR', None)
    ip = context['request'].META.get('HTTP_X_REAL_IP', None)
    # Default to US because of Event Volume
    country = 'USA'
    if not ip:
        # Set Default IP to SPE if no IP Available in Request
        ip = '192.152.183.80'
    if ip:
        loc = g.city(ip)
        if loc:
            country = loc['country_code3']
    try:
        region = Web_Region_Country.objects.get(country_UN=country).region
    except Web_Region_Country.DoesNotExist:
        region = 'USA'
    return region