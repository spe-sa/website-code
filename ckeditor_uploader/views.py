from __future__ import absolute_import

import os, sys
from datetime import datetime
from operator import itemgetter

from django.conf import settings
from django.core.files.storage import default_storage
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import generic
from django.views.decorators.csrf import csrf_exempt

from ckeditor_uploader import image_processing
from ckeditor_uploader import utils
from ckeditor_uploader.forms import SearchForm
from django.utils.html import escape
import logging

logger = logging.getLogger(__name__)

def get_upload_filename(upload_name, user):
    # If CKEDITOR_RESTRICT_BY_USER is True upload file to user specific path.
    if getattr(settings, 'CKEDITOR_RESTRICT_BY_USER', False):
        user_path = user.username
    else:
        user_path = ''

    # Generate date based path to put uploaded file.
    date_path = datetime.now().strftime('%Y/%m/%d')

    # Complete upload path (upload_path + date_path).
    upload_path = os.path.join(
        settings.CKEDITOR_UPLOAD_PATH, user_path, date_path)

    if getattr(settings, "CKEDITOR_UPLOAD_SLUGIFY_FILENAME", True):
        upload_name = utils.slugify_filename(upload_name)

    return default_storage.get_available_name(os.path.join(upload_path, upload_name))


class ImageUploadView(generic.View):
    http_method_names = ['post']

    def post(self, request, **kwargs):
        """
        Uploads a file and send back its URL to CKEditor.
        """
        uploaded_file = request.FILES['upload']

        backend = image_processing.get_backend()
        ck_func_num = escape(request.GET['CKEditorFuncNum'])

        # Throws an error when an non-image file are uploaded.
        if not getattr(settings, 'CKEDITOR_ALLOW_NONIMAGE_FILES', True):
            try:
                backend.image_verify(uploaded_file)
            except utils.NotAnImageException:
                return HttpResponse("""
                    <script type='text/javascript'>
                    window.parent.CKEDITOR.tools.callFunction({0}, '', 'Invalid file type.');
                    </script>""".format(ck_func_num))

        saved_path = self._save_file(request, uploaded_file)
        self._create_thumbnail_if_needed(backend, saved_path)
        url = utils.get_media_url(saved_path)

        # Respond with Javascript sending ckeditor upload url.
        return HttpResponse("""
        <script type='text/javascript'>
            window.parent.CKEDITOR.tools.callFunction({0}, '{1}');
        </script>""".format(ck_func_num, url))

    @staticmethod
    def _save_file(request, uploaded_file):
        filename = get_upload_filename(uploaded_file.name, request.user)
        saved_path = default_storage.save(filename, uploaded_file)
        return saved_path

    @staticmethod
    def _create_thumbnail_if_needed(backend, saved_path):
        if backend.should_create_thumbnail(saved_path):
            backend.create_thumbnail(saved_path)


upload = csrf_exempt(ImageUploadView.as_view())


def get_image_files(user=None, path=''):
    """
    Recursively walks all dirs under upload dir and generates a list of
    full paths for each file found.
    """
    # If a user is provided and CKEDITOR_RESTRICT_BY_USER is True,
    # limit images to user specific path, but not for superusers.
    STORAGE_DIRECTORIES = 0
    STORAGE_FILES = 1

    restrict = getattr(settings, 'CKEDITOR_RESTRICT_BY_USER', False)
    if user and not user.is_superuser and restrict:
        user_path = user.username
    else:
        user_path = ''

    browse_path = os.path.join(settings.CKEDITOR_UPLOAD_PATH, user_path, path)

    try:
        storage_list = default_storage.listdir(browse_path)
    except NotImplementedError:
        return
    except OSError:
        return

    for filename in storage_list[STORAGE_FILES]:
        if os.path.splitext(filename)[0].endswith('_thumb') or os.path.basename(filename).startswith('.'):
            continue
        filename = os.path.join(browse_path, filename)
        yield filename

    for directory in storage_list[STORAGE_DIRECTORIES]:
        if directory.startswith('.'):
            continue
        directory_path = os.path.join(path, directory)
        for element in get_image_files(user=user, path=directory_path):
            yield element


def get_files_browse_urls(user=None):
    """
    Recursively walks all dirs under upload dir and generates a list of
    thumbnail and full image URL's for each file found.
    """
    files = []
    for filename in get_image_files(user=user):
        src = utils.get_media_url(filename)
        if getattr(settings, 'CKEDITOR_IMAGE_BACKEND', None):
            if is_image(src):
                thumb = utils.get_media_url(utils.get_thumb_filename(filename))
            else:
                thumb = utils.get_icon_filename(filename)
            visible_filename = os.path.split(filename)[1]
            if len(visible_filename) > 20:
                visible_filename = visible_filename[0:19] + '...'
        else:
            thumb = src
            visible_filename = os.path.split(filename)[1]
        files.append({
            'thumb': thumb,
            'src': src,
            'is_image': is_image(src),
            'visible_filename': visible_filename,
        })

    return files


def is_image(path):
    ext = path.split('.')[-1].lower()
    return ext in ['jpg', 'jpeg', 'png', 'gif']

def get_relative_path(url):
    # attempt to strip the DATA_DIR and return what is left
    pos = url.find(settings.DATA_DIR)
    if pos > -1:
        pos = pos + len(settings.DATA_DIR)
        return url[pos:]
    else:
        return url


def browse(request):

    logger.debug('in browse...')
    file_type = 'File'
    param_type = request.GET.get('type', '')
    if param_type == 'image':
        file_type = 'Image'

    # dirs = get_directories(request.user)
    # get our directory
    # path = ''
    # browse_path = os.path.join(settings.MEDIA_ROOT, settings.CKEDITOR_UPLOAD_PATH, path)
    # # thumbnail_path = os.path.join(settings.DATA_DIR, settings.CKEDITOR_THUMBNAIL_PATH, path)
    # logger.debug("browse_path: %s", browse_path)
    # i=0
    # img_files = []
    # for root, dirs, files in os.walk(browse_path):
    #     # for name in dirs:
    #     #     logger.debug(os.path.join(root, name))
    #     if (i>=100):
    #         break
    #     for name in files:
    #         i=i+1
    #         if i>=100:
    #             break
    #         logger.debug(name)
    #         src = get_relative_path(os.path.join(root, name))
    #         img_files.append({
    #             'thumb': src.replace(settings.CKEDITOR_UPLOAD_PATH, settings.CKEDITOR_THUMBNAIL_PATH),
    #             'src': src,
    #             'is_image': is_image(src),
    #             'visible_filename': name,
    #         })
    #
    # logger.debug("image count: %s", i)
    #


    path = ''
    browse_path = os.path.join(settings.MEDIA_ROOT, settings.CKEDITOR_UPLOAD_PATH, path)
    # thumbnail_path = os.path.join(settings.DATA_DIR, settings.CKEDITOR_THUMBNAIL_PATH, path)
    logger.debug("browse_path: %s", browse_path)
    img_files = []
    i=0
    for root, dirs, files in os.walk(browse_path):
        # for name in dirs:
        #     logger.debug(os.path.join(root, name))
        for name in files:
            i=i+1
            logger.debug(name)
            full_filename = os.path.join(root, name)
            src = get_relative_path(full_filename)
            img_files.append({
                'thumb': src.replace(settings.CKEDITOR_UPLOAD_PATH, settings.CKEDITOR_THUMBNAIL_PATH),
                'src': src,
                'is_image': is_image(src),
                'visible_filename': name,
                'modified': os.path.getmtime(full_filename)
            })

    logger.debug("image count: %s", i)

    # for name in os.listdir(browse_path):
    #     # print all dirs
    #     if os.path.isdir(name):
    #         logger.debug(name)
    #
    # for name in os.listdir(browse_path):
    #     # print all files
    #     if not os.path.isdir(name):
    #         logger.debug(name)

    # img_files = get_files_browse_urls(request.user)
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data.get('q', '').lower()
            img_files = list(filter(lambda d: query in d['visible_filename'].lower(), img_files))
    else:
        form = SearchForm()

    show_dirs = getattr(settings, 'CKEDITOR_BROWSE_SHOW_DIRS', False)
    dir_list = sorted(set(os.path.dirname(f['src']) for f in img_files), reverse=True)

    logger.debug("sorting...")
    # sort our list by last modified date so we can pull the last 25 files
    # sorted(img_files, key=itemgetter(4), reverse=True)
    sorted(img_files, key=lambda image_props: image_props.get('modified', 0), reverse=True)  # sort by modified mtime
    logger.debug("sorted...")
    # grab the first 25 files in the sorted list to return to the view
    i=0
    show_files = []
    for img in img_files:
        if i >= 25:
            break
        if file_type == 'Image':
            if img.get('is_image') == True:
                # only move over images
                logger.debug("moving image: %s [%s]", img.get('src', ''), img.get('modified', ''))
                i = i + 1
                show_files.append(img)
            else:
                logger.debug("file [%s] is not an image skipping...", img.get('src', ''))
        else: # file type is File
            if img.get('is_image') == False:
                # only move over files that are not images
                logger.debug("moving file: %s [%s]", img.get('src', ''), img.get('modified', ''))
                i = i + 1
                show_files.append(img)
            else:
                logger.debug("file [%s] is an image skipping...", img.get('src', ''))

    logger.debug("moved %s files", i)


    # Ensures there are no objects created from Thumbs.db files - ran across this problem while developing on Windows
    # if os.name == 'nt':
    #     files = [f for f in files if os.path.basename(f['src']) != 'Thumbs.db']

    context = RequestContext(request, {
        'file_type': file_type,
        'show_dirs': show_dirs,
        'dirs': dir_list,
        'files': show_files,
        'form': form
    })
    return render_to_response('ckeditor/browse.html', context)
