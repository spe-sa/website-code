from django.conf import settings
from ..models import Customer
import logging
import bleach
import json


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
def get_context_variable(request, variable_name, default_value=None, ignoreDebug = False):
    debug = getattr(settings, "DEBUG", True)
    if ignoreDebug == True:
        debug = True
    header_name = variable_name.upper()
    value = request.META.get(header_name, None)
    if value is None:
        if not header_name.startswith("HTTP"):
            header_name = "HTTP-" + header_name
        value = request.META.get(header_name,
                                 getattr(settings, variable_name,
                                         request.COOKIES.get(variable_name, None)))
    if value is None and variable_name != 'cid' and variable_name != 'sm_constitid':
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
                     "vid": get_context_variable(request, "vid"),}
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
        if visitor and visitor.id and visitor.is_staff():
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
