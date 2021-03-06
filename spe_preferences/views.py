from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .forms import FindUserForm, PrefsForm, PrefsUserSearchForm, PrefsListForm, PrefsSubmissionForm
from .forms import PrefsUserSearchForm, ContactPrefsForm
from .models import Preference, ContactPreference, CustomerPreference, PreferenceGroup
from mainsite.models import Customer
    #, Countries
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
import re, time, socket, json, urllib


# def show_cookie(c):
#     print c
#     for key, morsel in c.iteritems():
#         print
#         print 'key =', morsel.key
#         print '  value =', morsel.value
#         print '  coded_value =', morsel.coded_value
#         for name in morsel.keys():
#             if morsel[name]:
#                 print '  %s = %s' % (name, morsel[name])

def myip():
    # determine the IP address that would be most publicly-visible
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("gmail.com", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip


# contact
@csrf_exempt
def contact_prefs(request):  #, user_vid=False, user_email=False, user_cid=False, user_loc=False):

    # if request.COOKIES['sm_constitid']:
    #     user_vid_cookie = request.COOKIES['vid']
    #     user_email_cookie = request.COOKIES['email']
    #     user_cid_cookie = request.COOKIES['sm_constitid']
    #     user_name1_cookie = request.COOKIES['first_name']
    #     user_name2_cookie = request.COOKIES['last_name']
    #     user_loc_cookie = request.COOKIES['countryCode']

    # allow for a constituent ID# and/or an email address to be passed in, as well as cookies
    # c = constituent_id_provided
    # e = email_address_provided
    # v = visitor_id_provided

    # if request.COOKIES['sm_constitid']:
    #     c = request.COOKIES['sm_constitid']
    # elif user_cid is not False:
    #     c = user_cid  # a provided value can override the cookie
    # else:
    #     c = ''
    #
    # if request.COOKIES['email']:
    #     e = request.COOKIES['email']
    # else:
    #     e = user_email  # provided value can override cookie
    #
    # if request.COOKIES['vid']:
    #     v = request.COOKIES['vid']
    # else:
    #     v = user_vid  # provided value can override cookie
    #
    # if request.COOKIES['countryCode']:
    #     l = request.COOKIES['countryCode']
    # else:
    #     l = user_loc  # provided value can override cookie

    v = request.POST.get('user_vid_given', None) or request.COOKIES.get('vid', '(not logged in)')
    e = urllib.unquote_plus(request.POST.get('user_email_given', '') or request.COOKIES.get('email', ''))
    c = request.POST.get('user_cid_given', None) or request.COOKIES.get('sm_constitid', '')
    l = request.POST.get('user_loc_given', None) or request.COOKIES.get('countryCode', '')

    users_found = None
    emsg = None
    if request.method == "POST":
        f = ContactPrefsForm(request.POST)
        f.when_submitted = timezone.now()
        f.user_vid_cookie = re.sub(r'[^0-9a-f-]', '', request.COOKIES.get('vid', '(not logged in)'))
        f.user_email_cookie = urllib.unquote_plus(request.COOKIES.get('email', '(not logged in)'))
        f.user_cid_cookie = request.COOKIES.get('sm_constitid', '(not logged in)')
        f.user_name1_cookie = request.COOKIES.get('first_name', '(not logged in)')
        f.user_name2_cookie = request.COOKIES.get('last_name', '(not logged in)')
        f.user_loc_cookie = request.COOKIES.get('countryCode', '(not logged in)')

        # f.data.csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', '')
        # cp_form = ContactPrefsForm(request.POST)

        # cp_form.user_vid = v
        # cp_form.user_email = e
        # cp_form.user_cid = c
        # cp_form.user_loc = l

        f.user_email_given = urllib.unquote_plus(request.POST.get('user_email_given', ''))
        f.user_name1_given = urllib.unquote_plus(request.POST.get('user_name1_given', ''))
        f.user_name2_given = urllib.unquote_plus(request.POST.get('user_name2_given', ''))
        # f.user_email_cookie = urllib.unquote_plus(request.COOKIES.get('email', '(not logged in)'))
        # f.user_name1_cookie = user_name1_cookie
        # f.user_name2_cookie = user_name2_cookie
        # f.user_vid_cookie = user_vid_cookie
        # f.user_cid_cookie = user_cid_cookie
        f.user_cid_given = urllib.unquote_plus(request.POST.get('user_cid_given', ''))
        f.user_loc_given = urllib.unquote_plus(request.POST.get('user_loc_given', ''))
        # f.user_loc_cookie = request.COOKIES.get('countryCode', '(not logged in)')

        f.promo_contact_via_pmail = request.POST.get('promo_contact_via_pmail', None)
        f.promo_contact_via_email = request.POST.get('promo_contact_via_email', None)

        f.email_sub_jpt = request.POST.get('email_sub_jpt', None)
        f.email_sub_ogf = request.POST.get('email_sub_ogf', None)
        f.email_sub_hse = request.POST.get('email_sub_hse', None)
        f.email_sub_twa = request.POST.get('email_sub_twa', None)
        f.email_sub_rdn = request.POST.get('email_sub_rdn', None)

        f.user_viewport_x = re.sub(r'[^0-9]', '', str(request.POST.get('user_viewport_x', '0')))
        f.user_viewport_y = re.sub(r'[^0-9]', '', str(request.POST.get('user_viewport_y', '0')))

        if True:  #f.is_valid():
            # cd = cp_form.cleaned_data

            # if cp_form.user_cid is not '':
            #     cp_form.user_cid = re.sub(r'[^0-9a-zA-Z]', '', cp_form.user_cid)  # a provided value can override the cookie
            # if request.COOKIES['sm_constitid'] is not '':
            #     cp_form.user_cid = re.sub(r'[^0-9a-zA-Z]', '', request.COOKIES['sm_constitid'])

#            cp_form.user_vid = request.POST.get('user_vid', request.COOKIES.get('vid', ''))

            # cp_form.user_vid = request.POST.get('user_vid', '')
            # if cp_form.user_vid == '':
            #     cp_form.user_vid = request.COOKIES.get('vid', '')

            # cp_form.user_email = request.META.get(request.POST['user_email'], request.get(request.COOKIES['email'], ''))
            # cp_form.user_cid = request.META.get(request.POST['user_cid'], request.get(request.COOKIES['sm_constitid'], ''))
            # cp_form.user_loc = request.META.get(request.POST['user_loc'], request.get(request.COOKIES['countryCode'], ''))

            # cp = cp_form.save(commit=False)
            # cp.when_submitted = timezone.now()
            # cp.save()

            # cp_form.user_vid_cookie=re.sub(r'[^0-9a-f-]', '', user_vid_cookie)
            # cp_form.user_email_cookie=urllib.unquote_plus(user_email_cookie)
            # cp_form.user_cid_cookie=user_cid_cookie
            # cp_form.user_loc_cookie=user_loc_cookie
            # cp_form.when_submitted = timezone.now()

# TODO re-factor this -- it works but screams that there must be a cleaner way -- maybe a simple flag to evaluate '0' as false, or at least do one chunk to loop over the fields instead of having a copied chunk for each one
            if request.POST.get('promo_contact_via_pmail', None) == '1':
                cvp = 1
            elif request.POST.get('promo_contact_via_pmail', None) == '0':
                cvp = 0
            else:
                cvp = None

            if request.POST.get('promo_contact_via_email', None) == '1':
                cve = 1
            elif request.POST.get('promo_contact_via_email', None) == '0':
                cve = 0
            else:
                cve = None

            if request.POST.get('email_sub_jpt', None) == '1':
                jpt = 1
            elif request.POST.get('email_sub_jpt', None) == '0':
                jpt = 0
            else:
                jpt = None

            if request.POST.get('email_sub_ogf', None) == '1':
                ogf = 1
            elif request.POST.get('email_sub_ogf', None) == '0':
                ogf = 0
            else:
                ogf = None

            if request.POST.get('email_sub_hse', None) == '1':
                hse = 1
            elif request.POST.get('email_sub_hse', None) == '0':
                hse = 0
            else:
                hse = None

            if request.POST.get('email_sub_twa', None) == '1':
                twa = 1
            elif request.POST.get('email_sub_twa', None) == '0':
                twa = 0
            else:
                twa = None

            if request.POST.get('email_sub_rdn', None) == '1':
                rdn = 1
            elif request.POST.get('email_sub_rdn', None) == '0':
                rdn = 0
            else:
                rdn = None


            #            esubs = request.POST.get('email_subscription_choices', None)
#            m = ContactPreference()
#             m = ContactPreference(
#                 user_vid_cookie=re.sub(r'[^0-9a-f-]', '', user_vid_cookie),
#                 user_email_cookie=urllib.unquote_plus(user_email_cookie),
#                 user_cid_cookie=user_cid_cookie,
#                 user_loc_cookie=user_loc_cookie,
#                 user_email_given=cp_form.user_email_given,
#                 # user_cid_given=cp_form.user_cid_given,
#                 # user_loc_given=cp_form.user_loc_given,
#                 # promo_contact_via_pmail=cp_form.promo_contact_via_pmail,
#                 # promo_contact_via_email=cp_form.promo_contact_via_email,
#                 email_subscription_jpt=cp_form.email_subscription_jpt,
#                 when_submitted = timezone.now()
#             )
#             m.save()
#             f.save()

            vc = re.sub(r'[^0-9a-f-]', '', str(request.COOKIES.get('vid', '')))
            ec = urllib.unquote_plus(str(request.COOKIES.get('email')))
            cc = re.sub(r'[^0-9a-fA-Z]', '', str(request.COOKIES.get('sm_constitid', '')))
            lc = re.sub(r'[^0-9a-fA-Z\.]', '', str(request.COOKIES.get('countryCode', '')))
            gc = urllib.unquote_plus(str(request.COOKIES.get('first_name')))
            fc = urllib.unquote_plus(str(request.COOKIES.get('last_name')))
            m = ContactPreference(
                promo_contact_via_pmail=cvp,
                promo_contact_via_email=cve,
                email_sub_jpt=jpt,
                email_sub_ogf=ogf,
                email_sub_hse=hse,
                email_sub_twa=twa,
                email_sub_rdn=rdn,
                user_email_given=f.user_email_given,
                user_cid_given=f.user_cid_given,
                user_loc_given=f.user_loc_given,
                user_name1_given=f.user_name1_given,
                user_name2_given=f.user_name2_given,
                user_mid_given=f.user_mid_given,
                user_vid_cookie=vc,
                user_email_cookie=ec,
                user_cid_cookie=cc,
                user_loc_cookie=lc,
                user_name1_cookie=gc,
                user_name2_cookie=fc,
                user_viewport_x=f.user_viewport_x,
                user_viewport_y=f.user_viewport_y,
                when_submitted=timezone.now()
            )
            m.save()


            #            users_found = Customer.objects.filter(id=cd.get('customer_id'))[:50].all()
            users_found = Customer.objects.filter(id=c)[:5].all()
            if not users_found:
                users_found = Customer.objects.filter(email=e)[:5].all()
            if users_found and users_found.count() == 1:
                for user in users_found:
                    user_cid = user.id
            if not users_found:
                request.session['emsg'] = "No Matches Found."
        else:
            return HttpResponse(
                '<h1>Line 180 -- POSTed form did not validate</h1><hr />'
                + '<h2>' + str(f.errors) + '</h2><hr />'
                + '<h2>' + str(f.non_field_errors) + '</h2><hr />'
                + '<h3>' + str(timezone.now()) + '</h3>'

                + '<br />'

                + "cvp = " + f.promo_contact_via_pmail + "<br />"
                + "cve = " + f.promo_contact_via_email + "<br />"
                + "jpt = " + f.email_sub_jpt + "<br />"
                + "ogf = " + f.email_sub_ogf + "<br />"
                + "hse = " + f.email_sub_hse + "<br />"
                + "twa = " + f.email_sub_twa + "<br />"
                + "rdn = " + f.email_sub_rdn + "<br />"

                + '<br />'

                + "Email Address (given) = " + f.user_email_given + "<br />"
                + "Name1 (given) = " + f.user_name1_given + "<br />"
                + "Name2 (given) = " + f.user_name2_given + "<br />"
                + "Constituent ID# (given) = " + f.user_cid_given + "<br />"
                + "Location (given) = " + f.user_loc_given + "<br />"

                + '<br />'

                + "Visitor UUID = " + f.user_vid_cookie + "<br />"

                + '<br />'

                + "Email Address (cookie) = " + f.user_email_cookie + "<br />"
                + "Name1 (cookie) = " + f.user_name1_cookie + "<br />"
                + "Name2 (cookie) = " + f.user_name2_cookie + "<br />"
                + "Constituent ID# (cookie) = " + f.user_cid_cookie + "<br />"
                + "Location (cookie) = " + f.user_loc_cookie + "<br />"

                + '<br />'

                + "Viewport X = " + f.user_viewport_x + "<br />"
                + "Viewport Y = " + f.user_viewport_y

            )

    elif request.method == "GET":
        precid = request.GET.get('cusid', '(no Marketo cusID/Personify #)')
        premid = request.GET.get('mktid', '(no Marketo mktID #)')
        preloc = request.GET.get('country', '(no Marketo locID/country code)')
        prepop = {'user_cid_given':precid, 'user_mid_given':premid, 'user_loc_given':preloc}

        f = ContactPrefsForm(request.GET, initial=prepop)
#        f = ContactPrefsForm(request.GET, user_loc_given=preloc)
#        f.user_loc_given = Countries()

        # cp_form.user_vid_given = user_vid_cookie
        # cp_form.user_email_given = user_email_cookie
        # cp_form.user_cid_given = user_cid_cookie
        # cp_form.user_loc_given = user_loc_cookie

#        user_cid = request.GET.get('user_cid', '')
    else:
        f = ContactPrefsForm()

    context = {'f': f, 'users_found': users_found, 'emsg': emsg}
    return render(request, 'spe_preferences/contact_prefs.html', context)


# contact
def xx703xxcontact_prefs(request):  #, user_vid=False, user_email=False, user_cid=False, user_loc=False):
    # allow for a constituent ID# and/or an email address to be passed in, as well as cookies
    # c = constituent_id_provided
    # e = email_address_provided
    # v = visitor_id_provided

    # if request.COOKIES['sm_constitid']:
    #     c = request.COOKIES['sm_constitid']
    # elif user_cid is not False:
    #     c = user_cid  # a provided value can override the cookie
    # else:
    #     c = ''
    #
    # if request.COOKIES['email']:
    #     e = request.COOKIES['email']
    # else:
    #     e = user_email  # provided value can override cookie
    #
    # if request.COOKIES['vid']:
    #     v = request.COOKIES['vid']
    # else:
    #     v = user_vid  # provided value can override cookie
    #
    # if request.COOKIES['countryCode']:
    #     l = request.COOKIES['countryCode']
    # else:
    #     l = user_loc  # provided value can override cookie

    v = request.POST.get('user_vid', None) or request.COOKIES.get('vid', '')
    e = re.sub('%40', '@', request.POST.get('user_email', '') or request.COOKIES.get('email', ''))
    c = request.POST.get('user_cid', None) or request.COOKIES.get('sm_constitid', '')
    l = request.POST.get('user_loc', None) or request.COOKIES.get('countryCode', '')

    users_found = None
    emsg = None
    if request.method == "POST":
        cp_form = ContactPrefsForm(request.POST)

        # cp_form.user_vid = v
        # cp_form.user_email = e
        # cp_form.user_cid = c
        # cp_form.user_loc = l

        if cp_form.is_valid():
            # cd = cp_form.cleaned_data

            # if cp_form.user_cid is not '':
            #     cp_form.user_cid = re.sub(r'[^0-9a-zA-Z]', '', cp_form.user_cid)  # a provided value can override the cookie
            # if request.COOKIES['sm_constitid'] is not '':
            #     cp_form.user_cid = re.sub(r'[^0-9a-zA-Z]', '', request.COOKIES['sm_constitid'])

#            cp_form.user_vid = request.POST.get('user_vid', request.COOKIES.get('vid', ''))

            # cp_form.user_vid = request.POST.get('user_vid', '')
            # if cp_form.user_vid == '':
            #     cp_form.user_vid = request.COOKIES.get('vid', '')

            # cp_form.user_email = request.META.get(request.POST['user_email'], request.get(request.COOKIES['email'], ''))
            # cp_form.user_cid = request.META.get(request.POST['user_cid'], request.get(request.COOKIES['sm_constitid'], ''))
            # cp_form.user_loc = request.META.get(request.POST['user_loc'], request.get(request.COOKIES['countryCode'], ''))

            # cp = cp_form.save(commit=False)
            # cp.when_submitted = timezone.now()
            # cp.save()

            # cp_form.when_submitted = timezone.now()
            # cp_form.save()

            if request.POST.get('promo_contact_via_pmail', None) == '1':
                cvp = 1
            elif request.POST.get('promo_contact_via_pmail', None) == '0':
                cvp = 0
            else:
                cvp = None

            if request.POST.get('promo_contact_via_email', None) == '1':
                cve = 1
            elif request.POST.get('promo_contact_via_email', None) == '0':
                cve = 0
            else:
                cve = None

            esubs = request.POST.get('email_subscription_choices', None)
            m = ContactPreference(user_vid=v, user_email=e, user_cid=c, user_loc=l, promo_contact_via_pmail=cvp, promo_contact_via_email=cve, email_subscription_choices=esubs)
            m.save()


            #            users_found = Customer.objects.filter(id=cd.get('customer_id'))[:50].all()
            users_found = Customer.objects.filter(id=c)[:5].all()
            if not users_found:
                users_found = Customer.objects.filter(email=e)[:5].all()
            if users_found and users_found.count() == 1:
                for user in users_found:
                    user_cid = user.id
            if not users_found:
                request.session['emsg'] = "No Matches Found."
    elif request.method == "GET":
        cp_form = ContactPrefsForm(request.GET)

        cp_form.user_vid = v
        cp_form.user_email = e
        cp_form.user_cid = c
        cp_form.user_loc = l

#        user_cid = request.GET.get('user_cid', '')
    else:
        cp_form = ContactPrefsForm()

    context = {'cp_form': cp_form, 'users_found': users_found, 'emsg': emsg}
    return render(request, 'spe_preferences/contact_prefs.html', context)

#     # allow for a constituent ID# and/or an email address to be passed in, as well as cookies
#     if constituent_id_provided:
#         c = constituent_id_provided
#     elif email_address_provided:
#         e = email_address_provided
#     elif visitor_id_provided:
#         v = visitor_id_provided
#     else:
#         if request.COOKIES['sm_constitid']:
#             c = request.COOKIES['sm_constitid']
#         else:
#             c = None
#         if request.COOKIES['email']:
#             e = request.COOKIES['email']
#         else:
#             e = None
#         if request.COOKIES['vid']:
#             v = request.COOKIES['vid']
#         else:
#             v = None
#
#     # choose the "best" identifier from what we have available
#     if c:
#         t = 'c'
# #        i = re.sub(r'[^0-9a-zA-Z]', '', c)
#         i = c
#     elif e:
#         t = 'e'
#         i = e
#     elif v:
#         t = 'v'
#         i = v
#     elif request.COOKIES['vid']:
#         t = 'v'
#         i = request.COOKIES['vid']
#     else:
#         t = '-'
#         i = '-'
#
#     users_found = None
#     saved = None
#     emsg = None
#     if request.method == "POST":
#         cp_form = ContactPrefsForm(request.POST)
#         if cp_form.is_valid():
#             cd = cp_form.cleaned_data
#             users_found = Customer.objects.filter(id=cd.get('customer_id'))[:50].all()
#             if not users_found:
#                 users_found = Customer.objects.filter(email=cd.get('email'))[:50].all()
#                 # if not users_found:
#                 #     users_found = Customer.objects.filter(first_name=cd.get('first_name'),
#                 #                                           last_name=cd.get('last_name'))[:50].all()
#                 # if not users_found:
#                 #     users_found = Customer.objects.filter(last_name=cd.get('last_name'))[:50].all()
#             if users_found and users_found.count() == 1:
#                 for user in users_found:
#                     user_id = user.id
#             if not users_found:
#                 request.session['emsg'] = "No Matches Found."
#                     # search_form.cid = user_id
#                     # search_form.fields["cid"].initial = user_id
#                     # search_form.cleaned_data['cid'] = user_id
#     elif request.method == "GET":
#         cp_form = ContactPrefsForm(request.GET)
#         user_id = request.GET.get('user_id', '')
#     else:
#         cp_form = ContactPrefsForm()
#
#     pgroups = PreferenceGroup.objects.filter(status='ACTIVE').order_by('category', 'sort_order', 'name')
#     pitems = Preference.objects.filter(status='ACTIVE').order_by('group_id', 'sort_order', 'name')
#     context = {'cp_form': cp_form, 'users_found': users_found, 'pgroups': pgroups, 'cid': user_id,
#                'saved': saved, 'emsg': emsg, 'pitems': pitems}
#     return render(request, 'spe_preferences/contact_prefs.html', context)


# who
def quick_find_user(request, email_address_provided=None, constituent_id_provided=None):

    # allow for a constituent ID# and/or an email address to be passed in, as well as cookies
    if constituent_id_provided:
        c = constituent_id_provided
    else:
        if request.COOKIES['sm_constitid']:
            c = request.COOKIES['sm_constitid']
        else:
            c = None
    if email_address_provided:
        e = email_address_provided
    else:
        if request.COOKIES['email']:
            e = request.COOKIES['email']
        else:
            e = None

    # choose the "best" identifier from what we have available
    if c:
        t = 'c'
#        i = re.sub(r'[^0-9a-zA-Z]', '', c)
        i = c
    elif e:
        t = 'e'
        i = e
    elif request.COOKIES['vid']:
        t = 'v'
        i = request.COOKIES['vid']
    else:
        t = '-'
        i = '-'
    s = 31536000 * 18 # 18 years, in seconds, for Max Age
    res = HttpResponse('ID Type = "' + t + '" and ID = "' + i + '"' + "\n")
    res.set_cookie(key='cp_id_type', value=t, max_age=s, domain='.spe.org', path='/', httponly=True, secure=True)
    res.set_cookie(key='cp_id', value=i, max_age=s, domain='.spe.org', path='/', httponly=True, secure=True)
    return res


# allow
def allow_communication_for(request, preferences_json=None, preference_code=None, yes_or_no=None, visitor_id_provided=None, email_address_provided=None, constituent_id_provided=None):
    ur = request.get_full_path()

    if preferences_json is None:
        if preference_code is not None and yes_or_no is not None:
            yn = str(yes_or_no).lower()[0:1]
            pj = str('{"' + str(preference_code).lower() + '": "' + yn + '"}')
        else:
            pj = '{}'
    else:
        pj = str(preferences_json)

    vi = visitor_id_provided or request.COOKIES['vid'] or 'b'
    ea = email_address_provided or request.COOKIES['email'] or 'b@d.tl'
    ci = constituent_id_provided or request.COOKIES['sm_constitid'] or '1'
    n1 = request.COOKIES['first_name'] or 'B.'
    n2 = request.COOKIES['last_name'] or 'F.'
    lc = request.get(request.COOKIES['location_code'], 'Texas')

    u = {}
    # {
    #     "vi": "8b14cdef-76fe-4cc7-9a10-a33039ce2eb4",
    #     "ea": "bfountain@spe.org",
    #     "n1": "Brett",
    #     "n2": "Fountain",
    #     "lc": "US.TX",
    #     "ci": "3415297",
    #     "ts": 1483566431,
    #     "tt": "5674986f95b1d0414a45a884a8320105b6edc849",
    #     "tv": "https://tls.spe.org/verify_trust_token"
    # }
    u['vi'] = vi
    u['ea'] = ea
    u['ci'] = ci
    u['n1'] = n1
    u['n2'] = n2
    u['lc'] = lc
    uj = json.dumps(u)

    return HttpResponse('<!-- allow_communication_for invoked at ' + ur + ' -->' + "<br /> Visitor UUID = " + vi + "<br /> Email Address = " + ea + "<br /> Constituent ID# = " + ci + "<hr />" + "<br /> Preferences JSON = " + pj + "<hr />" + "<br /> User JSON = " + uj)



# def hello_world(request):
#     return HttpResponse("Bonjour")


# def find_user(request):
#     users_found = None
#     if request.method == "POST":
#         form = FindUserForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             users_found = Customer.objects.filter(id=cd.get('constituent_id')).all()
#             if not users_found:
#                 users_found = Customer.objects.filter(email=cd.get('email')).all()
#                 if not users_found:
#                     users_found = Customer.objects.filter(first_name=cd.get('first_name'),
#                                                           last_name=cd.get('last_name')).all()
#
#                 #            form = FindUserForm()
#     else:
#         form = FindUserForm()
#     context = {'form': form, 'users_found': users_found}
#     return render(request, 'spe_preferences/search.html', context)


# def prefs_new(request):
#     saved = None
#     if request.method == "POST":
#         form = PrefsForm(request.POST)
#         if form.is_valid():
#             prefs = form.save(commit=False)
#             prefs.submitted_date = timezone.now()
#             prefs.save()
#             saved = True
#             form = PrefsForm()
#     else:
#         form = PrefsForm()
#     context = {'form': form, 'saved': saved}
#     return render(request, 'spe_preferences/base.html', context)


# called to search for a customer in our cache table
# also trigger for if we disable the search or the additional preferences selection
def additional_prefs_search(request):
    users_found = None
    user_id = ''
    saved = request.session.get('prefs_inserted', False)
    emsg = request.session.get('emsg', '')
    request.session['prefs_inserted'] = False
    request.session['emsg'] = ''

    #if request.COOKIES['sm_constitid'] and request.COOKIES['email'] and request.COOKIES['first_name'] and request.COOKIES['last_name'] and request.COOKIES['emeta_id'] and request.COOKIES['ERIGHTS']:
        # looks like we have cookies that were probably set by the real login
        # @TODO now we will decide how much to trust them
        #if request.COOKIES['tt']:
            # we have a tamper-evident token
            # if the token says it covers all the values we care about
                # if the server-side hash calculation matches what this token has
                    # values are trustworthy
    if request.COOKIES['sm_constitid']:
        users_found = Customer.objects.filter(id=re.sub(r'[^0-9a-z]', '', str(request.COOKIES['sm_constitid']).lower() ))[:50].all()
        if users_found and users_found.count() == 1:
            for user in users_found:
                user_id = user.id
    if request.method == "POST":
        search_form = PrefsUserSearchForm(request.POST)
        if search_form.is_valid():
            cd = search_form.cleaned_data
            if not users_found:
                users_found = Customer.objects.filter(id=cd.get('customer_id'))[:50].all()
                if not users_found:
                    users_found = Customer.objects.filter(email=cd.get('email'))[:50].all()
                    if not users_found:
                        users_found = Customer.objects.filter(first_name=cd.get('first_name'),
                                                              last_name=cd.get('last_name'))[:50].all()
                        if not users_found:
                            users_found = Customer.objects.filter(last_name=cd.get('last_name'))[:50].all()
            if users_found and users_found.count() == 1:
                for user in users_found:
                    user_id = user.id
            if not users_found:
                request.session['emsg'] = "No Matches Found."
                    # search_form.cid = user_id
                    # search_form.fields["cid"].initial = user_id
                    # search_form.cleaned_data['cid'] = user_id
    elif request.method == "GET":
        search_form = PrefsUserSearchForm(request.GET)
        user_id = request.GET.get('user_id', '') # BF701 - name is vague, both as to the data source and the intended ID (constit#? email? other?)
    else:
        search_form = PrefsUserSearchForm()

    pgroups = PreferenceGroup.objects.filter(status='ACTIVE').order_by('sort_order', 'category', 'name')
    pitems = Preference.objects.filter(status='ACTIVE').order_by('group_id', 'sort_order', 'name')
    context = {'search_form': search_form, 'users_found': users_found, 'pgroups': pgroups, 'cid': user_id,
               'saved': saved, 'emsg': emsg, 'pitems': pitems}
    return render(request, 'spe_preferences/content_interests.html', context)


# called to insert the membernumber and preferences into the database and then return a blank record with an alert
def additional_prefs_insert(request):
    if request.method == "POST":

        # this value should be manually updated
        # to match the official event code at which these preferences are being collected
        meeting_id = "16ATCE"

        customer_id = request.POST.get('customer_id', None)
        if customer_id:
            try:
                # remove all records for this guy for this meeting
                CustomerPreference.objects.filter(customer_id=customer_id, meeting_id=meeting_id).delete()
                # get a list of the groups selections will be applied to
                groups = PreferenceGroup.objects.filter(status='ACTIVE').all()
                for group in groups:
                    selection_list = request.POST.getlist('prefs_' + str(group.id))
                    for selection in selection_list:
                        id = int(selection)
                        p = Preference.objects.get(pk=id)
                        result = CustomerPreference()
                        result.meeting_id = meeting_id
                        result.customer_id = customer_id
                        result.preference = p
                        result.save()
                request.session['prefs_inserted'] = True
            except Exception as insert_e:
                request.session['emsg'] = insert_e
        else:
            request.session['emsg'] = "Customer id was not found with submission.  Unable to save."
    else:
        request.session['emsg'] = "Invalid save method.  Preferences were not saved."
    time.sleep(1)
    return redirect('add_prefs_search')


# def submit_prefs(request):
#     if request.method == "POST":
#         search_form = PrefsUserSearchForm(request.POST)
#         prefs_form = PrefsSubmissionForm(request.POST)
#         if prefs_form.is_valid():
#             prefs = prefs_form.save(commit=False)
#             prefs.when_submitted = timezone.now()
#             prefs.save()
#             return redirect('add_prefs_search', {'saved': True})
#     else:
#         prefs_form = PrefsForm()
#         search_form = FindUserForm()
#     context = { 'prefs_form': prefs_form, 'saved' : False, 'search_form': search_form}
#     return render(request, 'spe_preferences/submit_prefs.html', context)
