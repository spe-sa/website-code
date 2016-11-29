#from .models import SpeLink, SpeLinkCategory
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import os, time, datetime
from django.conf import settings
import json, fnmatch
from django.http import JsonResponse
from django.core.urlresolvers import reverse

import logging

logger = logging.getLogger(__name__)

def index(request):
    context = { }
    return render(request, 'spe_filer/index.html', context)

def detail(request, file_id):
    # link_category = get_object_or_404(SpeLinkCategory, pk=category_id)
    # links = SpeLink.objects.filter(category_id__exact=category_id).values()
    return render(request, 'spe_filer/detail.html', {'file_id': file_id })


def browse_json(request):
    param_path = request.POST.get('path', None)
    if not param_path:
        param_path = request.GET.get('path', '')

    files = getFileNames(request)
    # return HttpResponse(json.dumps(files), content_type="application/json")   # pre 1.7
    return JsonResponse(json.dumps(files), safe=False)
    # return {'files': files}

def modification_date(filename):
    return time.ctime(os.path.getmtime(filename))
    # t = os.path.getmtime(filename)
    # return datetime.datetime.fromtimestamp(t)

def browse(request):
    param_path = request.POST.get('path', None)
    if not param_path:
        param_path = request.GET.get('path', '')
    qs = request.META.get('QUERY_STRING', '')
    if qs:
        qs = '?' + qs
        pos = qs.find('&path=')
        if pos > -1:
            qs = qs[0:pos]
    breadcrumbs = []

    # set up our breadcrumbs
    # if we split just a / then we get 2 root entries so if slash make empty string
    if param_path == '/':
        param_path = ''
    paths = param_path.split("/")
    buildpath = ''
    for p in paths:
        bc = {}
        bc['name'] = p
        buildpath += '/' + p
        bc['buildpath'] = buildpath
        if p == '':
            bc['name'] = 'root'
            buildpath = ''
        breadcrumbs.append(bc)

    files = getFileNames(request)
    context = {
        'fs': files,
        'path': param_path,
        'breadcrumbs': breadcrumbs,
        'qs' : qs
    }
    return render(request, 'spe_filer/index.html', context)


def getFileNames(request):
    param_search = request.POST.get('search', None)
    if not param_search:
        param_search = request.GET.get('search', None)
    param_path = request.POST.get('path', None)
    if not param_path:
        param_path = request.GET.get('path', '')
    param_recursive = request.POST.get('recursive', None)
    if not param_recursive:
        param_recursive = request.GET.get('recursive', None)
    if param_recursive and param_recursive in ('1','t','true'):
        param_recursive = True
    else:
        param_recursive = False

    # make sure we never specify a path that goes outside our docroot area like /root or something; force relative
    param_path = param_path.strip()
    if param_path.startswith('/'):
        param_path = param_path [1:]
    path = os.path.join(settings.MEDIA_ROOT, param_path)
    furl = os.path.join(settings.MEDIA_URL, param_path)
    files = []
    if param_recursive:
        i = 0
        for root, dirnames, filenames in os.walk(path):
            if param_search:
                for filename in fnmatch.filter(filenames, param_search):
                    if filename.startswith('.'):
                        continue
                    file = {}
                    file['name'] = filename
                    file['path'] = root
                    file['type'] = 'f'
                    ffull = os.path.join(root, filename)
                    file['modified'] = modification_date(ffull)
                    file['size'] = os.stat(ffull).st_size
                    file['url'] = os.path.join(furl, filename)
                    files.append(file)
                    i+=1
                    if i >= 100:
                        break
            else:
                for filename in filenames:
                    if filename.startswith('.'):
                        continue
                    file = {}
                    file['name'] = filename
                    file['path'] = root
                    file['type'] = 'f'
                    ffull = os.path.join(root, filename)
                    file['modified'] = modification_date(ffull)
                    file['size'] = os.stat(ffull).st_size
                    file['url'] = os.path.join(furl, filename)
                    files.append(file)
                    i += 1
                    if i >= 100:
                        break
            if i >= 100:
                break
    else:
        fnames = os.listdir(path)
        if param_search:
            fnames = fnmatch.filter(fnames, param_search)

        for fname in fnames:
            if fname.startswith('.'):
                continue
            file = {}
            file['name'] = fname
            ffull = os.path.join(path, fname)
            if os.path.isdir(ffull):
                file['type'] = 'd'
            else:
                file['type'] = 'f'
            file['path'] = param_path
            file['modified'] = modification_date(ffull)
            file['url'] = os.path.join(furl, fname)
            file['size'] = os.stat(ffull).st_size
            files.append(file)
    return files


def addDirectory(request):
    # add our directory and re-show the listing page
    param_path = request.POST.get('path', None)
    if not param_path:
        param_path = request.GET.get('path', '')
    dir_name = request.POST.get('new_dir', None)
    if not dir_name:
        dir_name = request.GET.get('new_dir', None)
    print(dir_name)
    # if our path or new dir name starts with a slash remove it since that makes it root
    if param_path.startswith('/'):
        param_path = param_path[1:]
    if dir_name.startswith('/'):
        dir_name = dir_name[1:]
    fulldir = os.path.join(settings.MEDIA_ROOT, param_path, dir_name)
    if not os.path.exists(fulldir):
        os.makedirs(fulldir)
    param_qs = request.POST.get('qs', '')
    if param_qs:
        param_qs += '&path=' + param_path
    # return browse(request)
    return redirect(reverse('filebrowse') + param_qs)

def upload(request):
    param_path = request.POST.get('path', None)
    if not param_path:
        param_path = request.GET.get('path', '')
    # if our path or new dir name starts with a slash remove it since that makes it root
    if param_path.startswith('/'):
        param_path = param_path[1:]
    for afile in request.FILES.getlist('myfiles'):
        fullfile = os.path.join(settings.MEDIA_ROOT, param_path, afile.name)
        logger.info('uploading file: %s', afile)
        default_storage.save(fullfile, ContentFile(afile.read()))
        # afile.save(afile.name, afile.content, save=False)
    # print(request.FILES)
    param_qs = request.POST.get('qs', '')
    if param_qs:
        param_qs += '&path=' + param_path
    # return browse(request)
    return redirect(reverse('filebrowse') + param_qs)

