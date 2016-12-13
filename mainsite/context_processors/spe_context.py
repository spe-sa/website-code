from django.conf import settings
from ..models import Customer
import logging
import bleach
import json
import socket, struct

logger = logging.getLogger(__name__)

# A context processor to add the default information to the current Context
# - variables: from settings files
# - login: from cookies to show login/logout info and welcome msg
# - cookies: added to context for quick referencing
# - customer: added to context and cached for quick referencing
def set_default_values(request):

    variables = get_context_variables(request)

    customer = get_visitor(request)

    login = {'authenticated': (customer != None and
        get_context_variable(request, 'ERIGHTS', '') != '')}
    if login['authenticated']:
        login['command'] = 'logout'
        login['label'] = 'Sign Out'
    else:
        login['command'] = 'login'
        login['label'] = 'Sign In'
    # if localhost then lets use our login that sets cookies specifically for testing
    # otherwise we route to erights
    # check if httphost is not localhost or empty; otherwise use the address
    # NOTE: we can use sstacha-mac.spe.org on our local environment pointing to 127.0.0.1
    # !! cookies will work even authenticating against prod !!
    # determine if we are localhost
    is_localhost = False
    host = request.get_host()
    if host and (host.startswith('localhost') or host.startswith('127.0.0.1')):
        is_localhost = True
    if host == None or host == '':
        if get_context_variable(request, 'REMOTE_ADDR') == '127.0.0.1':
            is_localhost = True

    if is_localhost:
        login['url'] = "/localhost/" + str(login['command']) + "/"
    else:
        # build out the erights url for if we are not localhost
        login['target_url'] = request.build_absolute_uri(request.get_full_path())
        if login['command'] == 'logout':
            login['url'] = "/appssecured/login/servlet/LoginServlet?command=" + str(login['command'])
        else:
            login['url'] = "/appssecured/login/servlet/LoginServlet"

    # TODO: add more login stuff if needed

    # create the dataLayer json for appending to each gtm request
    dict_buffer = {}
    if login['authenticated']:
        dict_buffer['user'] = {}
        visitor_status = sanitize(get_context_variable(request, 'status', ''))
        variables['visitor_status'] = visitor_status
        dict_buffer['user']['memberStatus'] = visitor_status
        variables['visitor_id'] = customer.id
        dict_buffer['user']['id'] = customer.id
        if visitor_status != '':
            if visitor_status == 'Paid' or visitor_status == 'Unpaid':
                visitor_membership = 'Member'
                variables['visitor_membership'] = visitor_membership
                dict_buffer['user']['memberCustomer'] = visitor_membership
                is_student = sanitize(get_context_variable(request, 'student'))
                if is_student:
                    visitor_membership_type = 'Student'
                    variables['membership_type'] = visitor_membership_type
                    dict_buffer['user']['memberType'] = visitor_membership_type
                else:
                    visitor_membership_type = 'Professional'
                    variables['membership_type'] = visitor_membership_type
                    dict_buffer['user']['memberType'] = visitor_membership_type
            else:
                visitor_membership = 'Customer'
                variables['visitor_membership'] = visitor_membership
                dict_buffer['user']['memberCustomer'] = visitor_membership
    variables['gtm_dataLayer'] = json.dumps(dict_buffer)

    # NOTE: cookies are not generated so just append them to the context under cookies; no session info needed
    #logging.error('cookies - ' + str(request.COOKIES))

    return {
        'variables': variables,
        'cookies': request.COOKIES,
        'login': login,
        'visitor': customer,
    }

def sanitize(value):
    """
    removes images from the text
    """
    try:
        value = bleach.clean(value, strip=True)
        return value
    except:
        return ''


# environment variables are looked up:
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
    default_ip = getattr(settings, "DEFAULT_IP", '192.152.183.80')
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
    # finally before returning if private set to spe public address
    if variable_name.lower() == 'cip' and _is_private_ip(value):
        value = default_ip

    if value is None:
        value = default_value
    return value


def get_context_variables(request):
    # get the environment and debug variables from the config file
    #  NOTE: add to server side variables and check for future requests
    # try and read the dictionary value from the session; if not found then create it and put it in this session
    variables = None  # request.session.get('session_variables')
    if not variables:
        variables = {"ENVIRONMENT": get_context_variable(request, "ENVIRONMENT", "localhost"),
                     "DEBUG": get_context_variable(request, "DEBUG", True),
                     "DATA_DIR": get_context_variable(request, "DATA_DIR"),
                     "BASE_DIR": get_context_variable(request, "BASE_DIR"),
                     "PROJECT_DIR": get_context_variable(request, "PROJECT_DIR"),
                     "STATIC_URL": get_context_variable(request, "STATIC_URL"),
                     "MEDIA_URL": get_context_variable(request, "MEDIA_URL"),
                     "STATIC_ROOT": get_context_variable(request, "STATIC_ROOT"),
                     "MEDIA_ROOT": get_context_variable(request, "MEDIA_ROOT"),
                     "DEFAULT_IP": get_context_variable(request, "DEFAULT_IP"),
                     "vid": get_context_variable(request, "vid"),
                     "cip": get_ip(request)
                     }
        # TODO: add more expected variables here as needed from the settings files

        request.session['session_variables'] = variables
    # load in any variables we don't already have but are parameters
    # if dev then replace with parameters to make it easier to debug
    for key, value in request.GET.items():
        if key not in variables:
            variables[key] = get_context_variable(request, key)
    for key, value in request.POST.items():
        if key not in variables:
            variables[key] = get_context_variable(request, key)

    #logging.error('variables - ' + str(variables))
    return variables

def get_ip(request):
    if request.user.is_active and request.user.is_staff:
        _ip = get_context_variable(request, 'cip', None, True)
    else:
        _ip = get_context_variable(request, 'cip', None)
    return _ip

def get_visitor(request):
    debug = getattr(settings, "DEBUG", True)
    cid = get_context_variable(request, "cid")
    if not cid:
        cid = get_context_variable(request, "sm_constitid")
    # if our customerid changed then reset the login and customer cache
    visitor = request.session.get('session_visitor')
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
            log.debug("spe_context: Attempted to get Customer for pk=" + str(dba_id) + " but couldn't find one...")
            visitor = None
    # block to reset visitor ends...
    else:
        if visitor and visitor.id and unicode(visitor.id) != cid:
            request.session['session_visitor'] = None
            visitor = None
        if not visitor:
            # if there isn't a cid then there is no reason to try and load a customer.  just blank the session and return none
            if cid == None or cid == "":
                request.session['session_visitor'] = None
                return None

            # read the customer from db and cache it up
            try:
                visitor = Customer.objects.get(pk=cid)
                # visitor.set_achievement_token()
                request.session['session_visitor'] = visitor
            except Customer.DoesNotExist:
                log = logging.getLogger('website')
                log.debug("spe_context: Attempted to get Customer for pk=" + str(cid) + " but couldn't find one...")
                visitor = None

    #logging.error('customer - ' + str(visitor))
    # if visitor:
    #     logging.error('visitor call to is_officer: ' + str(visitor.has_classification("OFFICER")))
    return visitor

def _is_private_ip(ip):
    """Check if the IP belongs to private network blocks.
    @param ip: IP address to verify.
    @return: boolean representing whether the IP belongs or not to
             a private network block.
    """
    networks = [
        "0.0.0.0/8",
        "10.0.0.0/8",
        "100.64.0.0/10",
        "127.0.0.0/8",
        "169.254.0.0/16",
        "172.16.0.0/12",
        "192.0.0.0/24",
        "192.0.2.0/24",
        "192.88.99.0/24",
        "192.168.0.0/16",
        "198.18.0.0/15",
        "198.51.100.0/24",
        "203.0.113.0/24",
        "240.0.0.0/4",
        "255.255.255.255/32",
        "224.0.0.0/4",
    ]

    for network in networks:
        try:
            ipaddr = struct.unpack(">I", socket.inet_aton(ip))[0]

            netaddr, bits = network.split("/")

            network_low = struct.unpack(">I", socket.inet_aton(netaddr))[0]
            network_high = network_low | 1 << (32 - int(bits)) - 1

            if ipaddr <= network_high and ipaddr >= network_low:
                return True
        except Exception,err:
            continue

    return False