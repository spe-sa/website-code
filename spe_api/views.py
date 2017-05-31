from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests, json

# Create your views here.
class UrlValidation(View):
    def get(self, request):
        # we will attempt to validate every URL parameter passed in

        is_valid = True

        dict_buffer = {}
        # list_dicts = []

        items = request.GET.items()
        if not items:
            items = request.POST.items()
        for _key, _val in items:
            # build a json list and return it
            print(_key, _val)
            check_response = False
            check_status = 500

            try:
                r = requests.head(_val, allow_redirects=True)

                if r.status_code >= 200 and r.status_code < 400:
                    check_status = r.status_code
                    # if we were intercepted by a login screen then we treat that as a forbidden instead of success
                    if r.request.path_url.lower().startswith('/en/admin/login/' or r.request.path_url.lower().startswith('/admin/login/')):
                        # print('starts with login')
                        check_response = False
                        is_valid = False
                        check_status = 403
                    else:
                        check_response = True
                else:
                    check_response = False
                    is_valid = False

                dict_buffer[_key] = {}
                dict_buffer[_key]["response"] = check_response
                dict_buffer[_key]["status_code"] = check_status
                # list_dicts.append(dict_buffer)

            except Exception as e:
                is_valid = False
                dict_buffer[_key] = {}
                dict_buffer[_key]["response"] = False
                dict_buffer[_key]["status_code"] = 500
                # list_dicts.append(dict_buffer)

        # myurl = request.GET.get("myurl", None)
        # # try and do a lookup for the url passed
        # myresponse = False
        # mystatus = None
        # try:
        #     r = requests.head(myurl)
        #     if r.status_code >= 200 and r.status_code < 400:
        #         myresponse = True
        #     mystatus=r.status_code
        # except Exception as e:
        #     mystatus=500
        return JsonResponse({'valid': is_valid, 'results': dict_buffer})
