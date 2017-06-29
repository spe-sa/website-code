from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
import requests, json
from filer.models import File

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


class FilerLookup(View):
    def get(self, request):
        myurl = request.GET.get("url", None)
        myid = request.GET.get("id", None)

        print('myurl: ' + str(myurl))
        print('myid: ' + str(myid))
        # use johns code here to lookup the real id value for the url if id is not a number

        # if we didn't get an id passed we try to look one up by the url\
        # todo: determine if we need to do something with the options that we are not using atm
        # todo: consider doing 2 searches instead I suspect will be faster due to indexes
        if (myid == None or myid == '') and myurl != None and myurl != '':
            # try to look up the id by url or cononical url match
            # most likely regular url if no id so start with that
            # NOTE: trying file property looks like media is stripped
            search_url = myurl
            if search_url.startswith('/media/'):
                search_url = myurl[7:]
            images = File.objects.filter(file = search_url).get_real_instances()
            if images == None or len(images) == 0:
                # NOTE: i can't figure out how they get canonical_url since it is not stored; defaulting to looping
                # image = File.objects.filter(image__canonical_url__iexact = myurl).all()
                images = File.objects.all()
                for image in images:
                    if image.canonical_url == myurl:
                        myid = image.id
                        break
            else:
                myid = images[0].id

            # images = File.objects.all()
            # for image in images:
            #     if image.canonical_url == myurl:
            #         myid = image.id
            #         break
            #     if image.url == myurl:
            #         myid = image.id
            #         break

        return JsonResponse({'id': myid})
