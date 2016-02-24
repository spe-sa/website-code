
# A context processor to add the spe login cookie information to the current Context
#   primarily used in header for every page to determine logged in status, url, and welcome message
def set_login_values(request):

        # set the boolean authenticated variable
        spe_cookie_erights = request.COOKIES.get('ERIGHTS', '')
        spe_cookie_constit = request.COOKIES.get('sm_constitid','')
        spe_authenticated = (spe_cookie_erights != '' and spe_cookie_constit != '')
        # build out the name for the welcome message
        spe_cookie_first = request.COOKIES.get('first_name','')
        spe_cookie_last = request.COOKIES.get('last_name','')
        spe_name = ''
        if spe_cookie_first != '':
            spe_name = spe_cookie_first + " "
        spe_name += spe_cookie_last

        if spe_authenticated:
            spe_command = 'logout'
            spe_label = 'Sign Out'
        else:
            spe_command = 'login'
            spe_label = 'Sign In'

        # if our host is localhost or 127.0.0.1 then lets use our login that sets cookies specifically for testing otherwise we route to erights
        if request.META['REMOTE_ADDR'] == '127.0.0.1':
            spe_url = "/localhost/" + spe_command + "/"
        else:
            # build out the erights url for if we are not localhost
            spe_target_url = request.get_full_path()
            spe_url = "/appssecured/login/servlet/ErightsLoginServlet?g=ci&command=" + spe_command + "&ERIGHTS_TARGET=" + spe_target_url

        return {
            'spe_authenticated': spe_authenticated,
            'spe_name': spe_name,
            'spe_url': spe_url,
            'spe_label': spe_label,
        }

