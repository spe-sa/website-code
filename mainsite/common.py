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
def get_context_variable(request, variable_name, default_value=None, forceDebug=None):
    debug = forceDebug
    value = None
    if debug == None:
        debug = getattr(settings, "DEBUG", True)
    if debug == True and forceDebug == None:
        # if we are in debugging mode we can set to not debugging to mimic production; however, not reversed
        if 'debug' in request.POST:
            debug = to_bool(request.POST['debug'])
        if 'debug' in request.GET:
            debug = to_bool(request.GET['debug'])

    # reset the debug variable value if that is the variable we are looking for to take into account replacements
    if variable_name.lower() == 'debug':
        value = debug

    header_name = variable_name.upper()
    if value is None:
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
                 "login_id": get_visitor_id(request),
                 "dba_id": get_dba_id(request),
                 "is_debug": get_context_variable(request, "DEBUG", None),
                 }
    # TODO: add more expected variables here as needed from the settings files
    variables['is_local_ip'] = is_local_ip(variables['cip'])

    # request.session['session_variables'] = variables
    # # load in any variables we don't already have but are parameters
    # # if dev then replace with parameters to make it easier to debug
    # for key, value in request.GET.items():
    #     if key not in variables:
    #         variables[key] = get_context_variable(request, key)
    # for key, value in request.POST.items():
    #     if key not in variables:
    #         variables[key] = get_context_variable(request, key)

    # logging.error('variables - ' + str(variables))
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
    # re-writing this part because this doesn't work in production because the proxy prevents logging in on www.
    # we need to look at visitor but aviod doing the 2 db calls like the current code does today.
    # GOAL: if no login or dba then no database calls; if login but no dba 1 db call; if dba, 2 db calls.
    visitor_id = get_visitor_id(request)
    dba_id = get_dba_id(request)
    is_debug = get_context_variable(request, "DEBUG", None)
    visitor = None
    try:
        if to_bool(is_debug) and dba_id:
            visitor = Customer.objects.get(pk=dba_id)
        elif dba_id and request.user and request.user.is_authenticated and request.user.is_active and request.user.is_staff:
            visitor = Customer.objects.get(pk=dba_id)
        elif visitor_id:
            visitor = Customer.objects.get(pk=visitor_id)
            if visitor.is_staff() and dba_id and unicode(visitor.id) != dba_id:
                visitor = Customer.objects.get(pk=dba_id)
    except Customer.DoesNotExist:
        log = logging.getLogger('website')
        log.debug(
            "get_visitor: Attempted to get Customer for pk=" + unicode(visitor_id) + " or " + unicode(dba_id) + " but couldn't find one...")
    return visitor

def get_visitor_id(request):
    # NOTE: false says to not perform any substitutions based on the environment (treat like prod) unless parameter override
    visitor_id = get_context_variable(request, "cid", None, False)
    if not visitor_id:
        visitor_id = get_context_variable(request, "sm_constitid", None, False)
    return visitor_id

def get_dba_id(request):
    # NOTE: true says to not perform any substitutions based on the environment (treat like dev) unless parameter override
    visitor_id = get_context_variable(request, "cid", None, True)
    if not visitor_id:
        visitor_id = get_context_variable(request, "sm_constitid", None, True)
    return visitor_id


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
def is_local_ip(ip):
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

# def get_date_range(pStartDate, pEndDate, pTypeId, pTzCode, pTzOffset):
#     #
#     if pStartDate == None:
#         return ''
#     start_month = pStartDate.strftime("%a")
#     start_day = '%02d' % pStartDate.day
#     start_year = '%4d' % pStartDate.year
#     if pEndDate == None:
#         pEndDate = pStartDate
#     end_month = pEndDate.strftime("%a")
#     end_day = '%02d' % pEndDate.day
#     end_year = '%4d' % pEndDate.year
#     final_date = ''
#
#     if pTypeId == 1 or pTypeId == 6:
#         # webinars only make sense to use the startdate with the time portions they can not rage over days
#         final_date = start_day + " " + start_month + " " + start_year
#         # get the time portion in the format HH:MM <tz code> ( GMT- or +<tz_offset>)
#     else:
#         # everything else just shows the date portions (currently) and not the time portions but can span days.
#         # start with worse case example: 31 AUG - 2 SEP 2017
#         final_date = start_day + " " + start_month + " - " + end_day + " " + end_month + " " + start_year
#         # if our months are the same then compact it to just be the days changing like: 1 - 2 Aug 2017
#         if start_month == end_month:
#             final_date = start_day + " - " + end_day + " " + start_month + " " + start_year
#             # one more check to consolidate the days if it is the same too: 1 Aug 2017
#             if start_day == end_day:
#                 final_date = start_day + " " + start_month + " " + start_year
#
#     return final_date
#


def to_bool(s):
    if s == None:
        return False
    if s == 'True' or s == '1' or s == 1:
        return True
    elif s == 'False' or s == '0' or s == 0:
        return False
    else:
        return s