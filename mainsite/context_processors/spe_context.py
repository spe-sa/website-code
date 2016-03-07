from django.conf import settings
import logging

logger = logging.getLogger(__name__)


# A context processor to add the default information to the current Context
# - variables: from settings files
# - login: from cookies to show login/logout info and welcome msg
# - cookies: added to context for quick referencing
def set_default_values(request):
    # get the environment and debug variables from the config file
    #  NOTE: add to server side variables and check for future requests
    # try and read the dictionary value from the session; if not found then create it and put it in this session
    variables = request.session.get('session_variables')
    if not variables:
        variables = {}
        variables["ENVIRONMENT"] = get_context_variable(request, "ENVIRONMENT", "localhost")
        variables["DEBUG"] = get_context_variable(request, "DEBUG", True)
        # TODO: add more expected variables here as needed from the settings files
        request.session['session_variables'] = variables
    # load in any variables we don't already have but are parameters
    # if dev then replace with parameters to make it easier to debug
    for key, value in request.GET.items():
        # if debug then replace the value with the parameters
        if variables.get('DEBUG', False):
            variables[key] = value
        else:
            if key not in variables:
                variables[key] = get_context_variable(request, key)
    for key, value in request.POST.items():
        # if debug then replace the value with the parameters
        if variables.get('DEBUG', False):
            variables[key] = value
        else:
            if key not in variables:
                variables[key] = get_context_variable(request, key)

    logging.error('variables - ' + str(variables))

    # if our customerid changed then reset the login and customer cache
    customer = request.session.get('session_customer')
    if customer and customer.get('id') != get_context_variable(request, 'sm_constitid'):
        request.session['session_customer'] = None
        if request.session.get('session_login'):
            request.session['session_login'] = None

    login = request.session.get('session_login')
    if not login:
        login = {}
        login['authenticated'] = (get_context_variable(request, 'ERIGHTS' , '') != '' and get_context_variable(request, 'sm_constitid' , '') != '')
        if login['authenticated']:
            login['command'] = 'logout'
            login['label'] = 'Sign Out'
        else:
            login['command'] = 'login'
            login['label'] = 'Sign In'
        # if our host is localhost or 127.0.0.1 then lets use our login that sets cookies specifically for testing
        # otherwise we route to erights
        if get_context_variable(request, 'REMOTE_ADDR') == '127.0.0.1':
            login['url'] = "/localhost/" + login['command'] + "/"
        else:
            # build out the erights url for if we are not localhost
            login['target_url'] = request.get_full_path()
            login['url'] = "/appssecured/login/servlet/ErightsLoginServlet?g=ci&command=" + login['command'] + \
                           "&ERIGHTS_TARGET=" + login['target_url']

        # TODO: add more login stuff if needed
        request.session['session_login'] = login
    logging.error('login - ' + str(login))

    customer = request.session.get('session_customer')
    if not customer:
        customer = {}
        customer['name'] = get_context_variable(request, 'first_name', '')
        if customer['name']:
            customer['name'] += " "
        customer['name'] += get_context_variable(request, 'last_name', '')
        customer['email'] = get_context_variable(request, 'email')
        customer['id'] = get_context_variable(request, 'sm_constitid')
            # todo: add info from database read using the id
        # sample data for testing personalization
        customer['is_student'] = get_context_variable(request, 'is_student')
        customer['is_staff'] = get_context_variable(request, 'is_staff')
        # TODO: add more user stuff if needed
        request.session['session_customer'] = customer
    logging.error('customer - ' + str(customer))

    # NOTE: cookies are not generated so just append them to the context under cookies; no session info needed
    logging.error('cookies - ' + str(request.COOKIES))

    return {
        'variables': variables,
        'cookies': request.COOKIES,
        'login': login,
        'visitor': customer,
    }


# environment variables are looked up:
# - as a header
# - as a variable in settings file
# - as a cookie
# - if debug: as a parameter
# NOTE: first one found wins
def get_context_variable(request, variable_name, default_value = None):
    debug = getattr(settings, "DEBUG", True)
    header_name = variable_name.upper()
    value = request.META.get(header_name, None)
    if value is None:
        if not header_name.startswith("HTTP"):
            header_name = "HTTP-" + header_name
        value = request.META.get(header_name, getattr(settings, variable_name, request.COOKIES.get(variable_name, None)))
    if value is None and debug:
        if variable_name in request.POST:
            value = request.POST[variable_name]
        if value is None and variable_name in request.GET:
            value = request.GET[variable_name]
    if value is None:
        value = default_value
    return value