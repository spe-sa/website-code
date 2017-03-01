from django.contrib.gis.geoip import GeoIP
from netaddr import IPAddress
from mainsite.models import Web_Region_Country, Customer
from django.conf import settings
import logging, bleach

logger = logging.getLogger(__name__)

def getRegion(context):
    g = GeoIP()
    # ip = context['request'].META.get('REMOTE_ADDR', None)
    # ip = context['request'].META.get('HTTP_X_REAL_IP', None)
    ip = get_ip(context['request'])
    region = Web_Region_Country.objects.get(country_UN='USA').region
    if ip:
        loc = g.city(ip)
        if loc:
            country = loc['country_code3']
            try:
                region = Web_Region_Country.objects.get(country_UN=country).region
            except Web_Region_Country.DoesNotExist:
                region = Web_Region_Country.objects.get(country_UN='USA').region
    return region

# context variables are looked up:
# - as a header
# - as a variable in settings file
# - as a cookie
# - as a parameter
# NOTE: first one found wins unless debug=true then
# - as a parameter overwrites the others
# sas changing boolean to override to TRUE to forceDebug setting to what is passed
#       None (default): don't force anything (normal behavior to read the setting)
#       True: force debug = true mode (mostly for when we want to be debug in a production environment)
#       False: force debug = false (when we want the real logged in user and not an overridden parameter (dba))
def get_context_variable(request, variable_name, default_value=None, forceDebug = None):
    debug = forceDebug
    if debug == None:
        debug = getattr(settings, "DEBUG", True)
    header_name = variable_name.upper()
    value = request.META.get(header_name, None)
    if value is None:
        if not header_name.startswith("HTTP"):
            header_name = "HTTP-" + header_name
        value = request.META.get(header_name,
                                 getattr(settings, variable_name,
                                         request.COOKIES.get(variable_name, None)))
    if value is None and variable_name != 'cid' and variable_name != 'sm_constitid' and variable_name.lower() != 'cip':
        if variable_name in request.POST:
            value = request.POST[variable_name]
        if value is None and variable_name in request.GET:
            value = request.GET[variable_name]

    if debug == True:
        # overwrite anything already there if we have something
        if variable_name in request.POST:
            value = request.POST[variable_name]
        if value is None and variable_name in request.GET:
            value = request.GET[variable_name]

    # set our ip_address to the context for lookups with get context variable (cip)
    # NOTE: moving below variables so that gets picked up first
    if variable_name.lower() == 'cip' and value == None:
        # set to whatever the header is that mike sets from the proxy
        value = request.META.get('HTTP_X_REAL_IP', None)
        if not value:
            value = request.META.get('REMOTE_ADDR', None)

    if value is None:
        value = default_value
    return value


# NOTE: this will be loaded automatically for "pages" in the context
#
def get_context_variables(request):
    # get the environment and debug variables from the config file
    #  NOTE: add to server side variables and check for future requests
    # try and read the dictionary value from the session; if not found then create it and put it in this session
    # variables = None  # request.session.get('session_variables')
    # if not variables:

    variables = {"ENVIRONMENT": get_context_variable(request, "ENVIRONMENT", "localhost"),
                 "DEBUG": get_context_variable(request, "DEBUG", True),
                 "HIDE_ADSPEED": get_context_variable(request, "HIDE_ADSPEED", False),
                 "DATA_DIR": get_context_variable(request, "DATA_DIR"),
                 "BASE_DIR": get_context_variable(request, "BASE_DIR"),
                 "PROJECT_DIR": get_context_variable(request, "PROJECT_DIR"),
                 "STATIC_URL": get_context_variable(request, "STATIC_URL"),
                 "MEDIA_URL": get_context_variable(request, "MEDIA_URL"),
                 "STATIC_ROOT": get_context_variable(request, "STATIC_ROOT"),
                 "MEDIA_ROOT": get_context_variable(request, "MEDIA_ROOT"),
                 "DEFAULT_IP": get_context_variable(request, "DEFAULT_IP"),
                 "vid": get_context_variable(request, "vid"),
                 "cip": get_ip(request),
                 }
    # TODO: add more expected variables here as needed from the settings files
    variables['is_private'] = is_private_ip(variables['cip'])

        # request.session['session_variables'] = variables
    # # load in any variables we don't already have but are parameters
    # # if dev then replace with parameters to make it easier to debug
    # for key, value in request.GET.items():
    #     if key not in variables:
    #         variables[key] = get_context_variable(request, key)
    # for key, value in request.POST.items():
    #     if key not in variables:
    #         variables[key] = get_context_variable(request, key)

    #logging.error('variables - ' + str(variables))
    return variables


# NOTE: the user object holds the django logged in user; this is for the authenticated visitor of the website if any
#   the website visitor object is essentially the Customer model in mainsite
#
# website visitors are looked up:
# - from the cid (header, setting, cookie, parameter)
# - from the sm_constitid (header, setting, cookie, parameter)
#
# NOTE: first one found wins unless debug=true then
# - as a parameter overwrites the others if the logged in django user is staff.  This gives staff the ability to
#   be someone else by being logged into django and putting a cid variable as a parameter in any environment

def get_visitor(request):
    debug = getattr(settings, "DEBUG", True)
    cid = get_context_variable(request, "cid")
    if not cid:
        cid = get_context_variable(request, "sm_constitid")
    # if our customerid changed then reset the login and customer cache
    visitor = None
    # visitor = request.session.get('session_visitor')

    # sas 2016-01-03: adding snippit to look for any parameters if we are staff on every request.
    #   this will allow testing in prod exactly like qa and dev but only for staff members
    dba_id = None
    # if we are production and staff then try to load the visitor again ignoring debug flag (don't save back to session)
    if debug == False:
        # changing from using visitor object to using built in user is_staff setting
        # if visitor and visitor.id and visitor.is_staff():
        # NOTE: can have an unauthenticated AnonymousUser returned
        thisUser = request.user
        if thisUser and thisUser.is_authenticated and thisUser.is_active and thisUser.is_staff:
            dba_id = get_context_variable(request, "cid", None, True)
        if not dba_id:
            dba_id = get_context_variable(request, "sm_constitid", None, True)
    if dba_id and dba_id != cid and debug==False:
        try:
            visitor = Customer.objects.get(pk=dba_id)
        except Customer.DoesNotExist:
            log = logging.getLogger('website')
            log.debug("get_visitor: Attempted to get Customer for pk=" + str(dba_id) + " but couldn't find one...")
            visitor = None
    # block to reset visitor ends...
    else:
        if visitor and visitor.id and unicode(visitor.id) != cid:
            # request.session['session_visitor'] = None
            visitor = None
        if not visitor:
            # if there isn't a cid then there is no reason to try and load a customer.  just blank the session and return none
            if cid == None or cid == "":
                # request.session['session_visitor'] = None
                return None

            # read the customer from db and cache it up
            try:
                visitor = Customer.objects.get(pk=cid)
                # visitor.set_achievement_token()
                # request.session['session_visitor'] = visitor
            except Customer.DoesNotExist:
                log = logging.getLogger('website')
                log.debug("get_visitor: Attempted to get Customer for pk=" + str(cid) + " but couldn't find one...")
                visitor = None

    #logging.error('customer - ' + str(visitor))
    # if visitor:
    #     logging.error('visitor call to is_officer: ' + str(visitor.has_classification("OFFICER")))
    return visitor

# the preferable way to look up the visitors ip address.  Allows staff logged in user to override with cip variable
#
def get_ip(request):
    if request.user.is_active and request.user.is_staff:
        _ip = get_context_variable(request, 'cip', None, True)
    else:
        _ip = get_context_variable(request, 'cip', None)
    return _ip

# determines if the passed ip is a non-routeable address.  NOTE: currently doesn't take into account our DMZ address ranges
#
def is_private_ip(ip):
    if (ip == '127.0.0.1'):
        return True
    return IPAddress(ip).is_private()


# sanitizes a value if possible
# NOTE: should be used on all values that come from input like form submissions and such.
# NOTE: if using django form then this is not needed; they are processed for you.  Only needed for retrieval from
#   the request object
#
def sanitize(value):
    """
    removes images from the text
    """
    try:
        value = bleach.clean(value, strip=True)
        return value
    except:
        return ''
