import os

gettext = lambda s: s


"""
Django settings for mainsite project.

Generated by 'django-admin startproject' using Django 1.8.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/

See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

"""
# APP_DIR is the main application directory (mainsite for us)
APP_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# PROJECT_DIR is the directory that is the django project (website for us)
PROJECT_DIR = os.path.dirname(APP_DIR)
# BASE_DIR: is whatever directory contains your environment and project directory (djangocms for me)
BASE_DIR = os.path.dirname(PROJECT_DIR)
# DATA_DIR: is the directory containing our data (database? staticfiles? media?)
DATA_DIR = os.path.join(BASE_DIR, 'website_content')
# DATA_DIR = os.path.dirname(os.path.dirname(__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@$%x*kpb@)n3tmc$7k^lb18aovbmp&g+ai7@py0rd*)4g(a(_7'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition
ROOT_URLCONF = 'mainsite.urls'
WSGI_APPLICATION = 'mainsite.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'America/Chicago'

USE_I18N = True
USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(BASE_DIR, 'website_static')
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))

STATICFILES_DIRS = (
    # os.path.join(PROJECT_PATH, ""),
    os.path.join(BASE_DIR, 'website/spe_events', 'static'),
)

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(APP_DIR, 'templates'), ],
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.i18n',
                'django.core.context_processors.debug',
                'django.core.context_processors.request',
                'django.core.context_processors.media',
                'django.core.context_processors.csrf',
                'django.core.context_processors.tz',
                'sekizai.context_processors.sekizai',
                'django.core.context_processors.static',
                'cms.context_processors.cms_settings',
                'mainsite.context_processors.spe_context.set_default_values',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
                'django.template.loaders.eggs.Loader'
            ],
        },
    },
]

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'mainsite.middleware.visitor.CustomerMiddleware',
    'mainsite.middleware.visitor.VisitorMiddleware',
    'reversion.middleware.RevisionMiddleware',
    'request.middleware.RequestMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'admin_shortcuts',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'djangocms_page_sitemap',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_text_ckeditor',
    'djangocms_style',
    'djangocms_column',
    'easy_thumbnails',
    # 'filer',
    'config.apps.FilerConfig',
    #    'mptt',
    'ckeditor',
    'ckeditor_filebrowser_filer',
    'ckeditor_uploader',
    # 'cmsplugin_filer_image',
    'config.apps.FilerPluginConfig',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_utils',
    'cmsplugin_filer_video',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    # 'djangocms_picture',
    'easy_select2',
    'reversion',
    'config.apps.MainsiteConfig',
    'segmentation',
    # 'smartsnippets',
    #'config.apps.SmartsnippetConfig',
    'taggit',
    # 'spe_links',
    'config.apps.SpeLinkConfig',
    # 'spe_blog',
    'config.apps.SpeBlogConfig',
    'google_tag_manager',
    #    'spe_contact',
    'config.apps.SpePollConfig',
    # 'spe_polls',
    # 'request',
    'config.apps.RequestConfig',
    # 'spe_events',
    'config.apps.SpeEventConfig',
    'djangocms_forms',
    'cmsplugin_bootstrap_columns',
    'spe_preferences',
    # 'django_extensions',
    'dashing',
    'dashboard',
    'config.apps.SpePromotions',
    # 'carousel',
    'django_fsm',
    'spe_messages',
    'adminsortable',
    'config.apps.SpeCustomMenus',
    'spe_sponsors',
    'spe_ui_components',
    # 'model_report',
    'config.apps.SpeCustomAgendaConfig',
    'tastypie',
    'colorfield',
    'spe_custom_scrollspy',
    # 'statsy',
    # 'controlcenter',
    'imagekit',
    'django_countries',
    'spe_api',
    # 'aldryn_bootstrap3',
    # 'djangocms_history', # for DjangoCMS 3.4 upgrade (history is now separate)
)

LANGUAGES = (
    # Customize this
    ('en', gettext('en')),
    ('es', gettext('es')),
    ('ru', gettext('ru')),
    ('zh-cn', gettext('zh-cn')),
)

CMS_LANGUAGES = {
    # Customize this
    'default': {
        'public': True,
        'hide_untranslated': False,
        'redirect_on_fallback': True,
    },
    1: [
        {
            'public': True,
            'code': 'en',
            'hide_untranslated': False,
            'name': gettext('en'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'es',
            'hide_untranslated': False,
            'name': gettext('es'),
            'redirect_on_fallback': True,
        },
        {
            'public': True,
            'code': 'ru',
            'hide_untranslated': False,
            'name': gettext('ru'),
            'redirect_on_fallback': True,
        },
{
            'public': True,
            'code': 'zh-cn',
            'hide_untranslated': False,
            'name': gettext('zh-cn'),
            'redirect_on_fallback': True,
        },
    ],
}

CMS_TEMPLATES = (
    ('www_3col.html', 'WWW 3 Column page & Homepage'),
    ('www_subpage.html', 'WWW SubPage'),
    ('ogf_home.html', 'OGF Homepage'),
    ('ogf_subpage.html', 'OGF SubPage'),
    ('jpt_home.html', 'JPT Homepage'),
    ('jpt_subpage.html', 'JPT SubPage'),
    ('hse_home.html', 'HSE Homepage'),
    ('hse_subpage.html', 'HSE SubPage'),
    ('twa_home.html', 'TWA Homepage'),
    ('twa_subpage.html', 'TWA SubPage'),
    ('iptcnet/iptcnet_homepage.html', 'IPTCNET Home'),
    ('iptcnet/iptcnet_subpage.html', 'IPTCNET Sub'),
    ('iptcnet/iptcnet_subpage_rightcol.html', 'IPTCNET Sub Rt Col'),
    ('generic_page.html', 'Generic Page'),
    ('print_base.html', 'Print Page'),
    ('bootstrap_full_width.html', 'Bootstrap Generic Full Width'),
    ('atce/atce_homepage.html', 'ATCE Homepage'),
    ('atce/atce_subpage.html', 'ATCE Subpage'),
    ('iptc/iptc_homepage.html', 'IPTC Homepage'),
    ('iptc/iptc_subpage.html', 'IPTC Subpage'),
    ('iptc/iptc_subpage_rightcol.html', 'IPTC Subpage Right Col'),
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {
    'content': {
        'plugins': ['ShowTextPlugin',
                    'ShowAdSpeedZonePlugin',
                    'ShowTitlePlugin',
                    'ShowTileImgBack',
                    # filer plugins
                    'FilerFilePlugin',
                    'FilerFolderPlugin',
                    'FilerImagePlugin',
                    'FilerVideoPlugin',
                    # Generic plugins
                    'GoogleMapPlugin',
                    # 'InheritPagePlaceholderPlugin',
                    'LinkPlugin',
                    # 'StylePlugin',
                    # links plugin
                    'SpeLinkPluginPublisher',
                    # multi-column
                    'MultiColumnPlugin',
                    # forms
                    'FormPlugin',
                    # blog
                    'ShowArticleDetailPlugin',
                    'ShowArticlesPlugin',
                    'ShowArticlesListingPlugin',
                    'ShowBriefDetailPlugin',
                    'ShowBriefPlugin',
                    'ShowBriefListingPlugin',
                    'ShowArticleAndBriefPlugin',
                    # 'ShowEditorialPlugin',
                    'ShowIssuesByPublicationPlugin',
                    'ShowIssuesByYearPlugin',
                    'ShowMarketoFormPlugin',
                    'ShowMarketoFormWithoutThankYouPlugin',
                    'ShowTopicsListPlugin',
                    'ShowTopicsListingPlugin',
                    'ShowTagsDetailPlugin',
                    'ShowTagTitlePlugin',
                    'ShowTopicTitlePlugin',
                    # snippets
                    #'SmartSnippetPlugin',
                    # events
                    'ShowEventsByCurrentLocationPluginPlugin',
                    'PollPlugin',
                    # segmentation
                    'SegmentLimitPlugin',
                    'BootStrapContainerPlugin',
                    'BootstrapRowPlugin',
                    'ShowHorizontalBar',
                    # spe_promotions
                    'ShowEventNearLocationPromotionListing',
                    'ShowEventNearUserPromotionListing',
                    'ShowEventsByDisciplineListingPlugin',
                    'ShowEventsByTopicListingPlugin',
                    'ShowEventsByRegionListingPlugin',
                    'ShowEventsListingPlugin',
                    'ShowEventInUserRegionPromotionListing',
                    'ShowEventsForMemberPlugin',
                    'ShowUpcomingEventsListingPlugin',
                    'MembershipPromotionSelectionPlugin',
                    'BlogPlugin',
                    'BlogListingPlugin',
                    'BlogDetailPlugin',
                    'ShowMessagesToMemberPlugin',
                    'TabHeaderPlugin',
                    'TabPlugin',
                    'CustomMenuPluginInstance',
                    'PanelPlugin',
                    'AccordionHeaderPlugin',
                    'AccordionPlugin',
                    'SPECarouselHeaderPlugin',
                    'SPECarouselPlugin',
                    'PageLinkSetPluginInstance',
                    'StylePlugin',
                    'JumbotronPlugin',
                    'CustomAgendaPluginInstance',
                    'ModalPlugin',
                    'ModalBodyPlugin',
                    'ModalFooterPlugin',
                    'ModalHeaderPlugin',
                    'ContainerPlugin',
                    'CustomColumnPlugin',
                    'CustomRowPlugin',
                    'ScrollSpyHeaderPlugin',
                    'ScrollSpyPlugin',
                    'SpacerPlugPlugin',
                    'SingleLinkPlugin',
                    'CalendarEventItemPlugin',
                    'ImageItemPluginInstance',
                    # 'Bootstrap3RowCMSPlugin',
                    # 'Bootstrap3ColumnCMSPlugin',
                    # 'Bootstrap3BlockquoteCMSPlugin',
                    # 'Bootstrap3CiteCMSPlugin',
                    # 'Bootstrap3ButtonCMSPlugin',
                    # 'Bootstrap3CodeCMSPlugin',
                    # 'Bootstrap3ImageCMSPlugin',
                    # 'Bootstrap3ResponsiveCMSPlugin',
                    # 'Bootstrap3IconCMSPlugin',
                    # 'Bootstrap3LabelCMSPlugin',
                    # 'Bootstrap3JumbotronCMSPlugin',
                    # 'Bootstrap3AlertCMSPlugin',
                    # 'Bootstrap3ListGroupCMSPlugin',
                    # 'Bootstrap3ListGroupItemCMSPlugin',
                    # 'Bootstrap3PanelCMSPlugin',
                    # 'Bootstrap3PanelHeadingCMSPlugin',
                    # 'Bootstrap3PanelBodyCMSPlugin',
                    # 'Bootstrap3PanelFooterCMSPlugin',
                    # 'Bootstrap3WellCMSPlugin',
                    # 'Bootstrap3TabCMSPlugin',
                    # 'Bootstrap3TabItemCMSPlugin',
                    # 'Bootstrap3AccordionCMSPlugin',
                    # 'Bootstrap3AccordionItemCMSPlugin',
                    # 'Bootstrap3CarouselCMSPlugin',
                    # 'Bootstrap3CarouselSlideCMSPlugin',
                    # 'Bootstrap3SpacerCMSPlugin',
                    # 'Bootstrap3FileCMSPlugin',
                    ],
        'child_classes': {
            'SegmentLimitPlugin': [
                'ShowTextPlugin',
                'ShowAdSpeedZonePlugin',
                'ShowTitlePlugin',
                'ShowTileImgBack',
                # filer plugins
                'FilerFilePlugin',
                'FilerFolderPlugin',
                'FilerImagePlugin',
                'FilerVideoPlugin',
                # Generic plugins
                'GoogleMapPlugin',
                # 'InheritPagePlaceholderPlugin',
                'LinkPlugin',
                # 'StylePlugin',
                # links plugin
                'SpeLinkPluginPublisher',
                # multi-column
                'MultiColumnPlugin',
                # forms
                'FormPlugin',
                # blog
                'ShowArticleDetailPlugin',
                'ShowArticlesPlugin',
                'ShowArticlesListingPlugin',
                'ShowBriefDetailPlugin',
                'ShowBriefPlugin',
                'ShowBriefListingPlugin',
                # 'ShowEditorialPlugin',
                'ShowIssuesByPublicationPlugin',
                'ShowIssuesByYearPlugin',
                'ShowMarketoFormPlugin',
                'ShowMarketoFormWithoutThankYouPlugin',
                'ShowTopicsListPlugin',
                'ShowTopicsListingPlugin',
                'ShowTagsDetailPlugin',
                'ShowTagTitlePlugin',
                'ShowTopicTitlePlugin',
                # snippets
                # 'SmartSnippetPlugin',
                # events
                'ShowEventsByCurrentLocationPluginPlugin',
                'PollPlugin',
                # segmentation
                'SegmentLimitPlugin',
                'CookieSegmentPlugin',
                'VariableSegmentPlugin',
                'VisitorSegmentPlugin',
                'VisitorPropertySegmentPlugin',
                'VisitorClassificationSegmentPlugin',
                'FallbackSegmentPlugin',
                'DisciplineSegmentPlugin',
                'CountrySegmentPlugin',
                'BootstrapColumnPlugin',
                'VisitorDisciplineSegmentPlugin',
                'VisitorRegionSegmentPlugin',
                'VisitorDisciplineSegmentPlugin',
                'VisitorMembershipPaidSegmentPlugin',
                'VisitorMembershipYearPaidSegmentPlugin',
                'VisitorIPtoRegionSegmentPlugin',
                'DateTimeSegmentPlugin',
            ],
        },
        'plugin_modules': {
            'LinkPlugin': 'Links',
            'GoogleMapPlugin': 'Components',
            # 'StylePlugin': 'Components',
        },

    },
    'notice': {
        'inherit': 'content',
    },
    'secondary content': {
        'inherit': 'content',
    },
    'tertiary content': {
        'inherit': 'content',
    },
    'feature': {
        # 'inherit': 'content',
    },
    # 'editorial': {
    #     'inherit': 'content',
    # },
    'content title': {
        'inherit': 'content',
    },
    'page title': {
        'inherit': 'content',
    },
    'title area': {
        'inherit': 'content',
    },

}

MIGRATION_MODULES = {
    'cmsplugin_filer_image': 'cmsplugin_filer_image.migrations_django',
    'cmsplugin_filer_file': 'cmsplugin_filer_file.migrations_django',
    'cmsplugin_filer_folder': 'cmsplugin_filer_folder.migrations_django',
    'cmsplugin_filer_video': 'cmsplugin_filer_video.migrations_django',
    'cmsplugin_filer_teaser': 'cmsplugin_filer_teaser.migrations_django'
}

TAGGIT_CASE_INSENSITIVE = True

# GeoIP Configuration

GEOIP_PATH = os.path.join(PROJECT_DIR, 'data', 'GeoIP')

# LOGFILE_NAME = os.path.join(BASE_DIR, 'output.log')

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        # 'file': {
        #     'level': 'DEBUG',
        #     'class': 'logging.FileHandler',
        #     'filename': LOGFILE_NAME,
        #     'formatter': 'verbose'
        #     },
    },
    'loggers': {
        'root': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'website': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        }
    }
}

# email Configuration

EMAIL_HOST = "relaydev.spe.org"
EMAIL_DEFAULT_FROM = "support@spe.org"
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
MANAGERS = (('IT', 'webmaster@spe.org'),)

# config.contentsCss = 'http://localhost:8000/static/www/css/inline.css';


# Request Tracking

# REQUEST_TRAFFIC_MODULES = (
#    'request.traffic.UniqueVisitor',
#    'request.traffic.UniqueVisit',
#    'request.traffic.Hit',
#    'request.traffic.Ajax',
#    'request.traffic.NotAjax',
#    'request.traffic.Error',
#    'request.traffic.Error404',
#    'request.traffic.Search',
#    'request.traffic.Secure',
#    'request.traffic.Unsecure',
#    'request.traffic.User',
#    'request.traffic.UniqueUser',
# )

REQUEST_PLUGINS = (
    'request.plugins.TrafficInformation',
    'request.plugins.LatestRequests',
    'request.plugins.TopPaths',
    'request.plugins.TopErrorPaths',
    'request.plugins.TopReferrers',
    'request.plugins.TopSearchPhrases',
    'request.plugins.TopBrowsers',
    'request.plugins.ActiveUsers',
)

# Event Personalization Server Configuration

EVENT_PERSONALIZATION_SERVER = ('http://iisdev1/iappsint/p13ndemo/api/I2KTaxonomy/GetEventList3')

# Djangocms_forms Configurations

# DJANGOCMS_FORMS_RECAPTCHA_PUBLIC_KEY = '<recaptcha_site_key>'
# DJANGOCMS_FORMS_RECAPTCHA_SECRET_KEY = '<recaptcha_secret_key>'

DJANGOCMS_FORMS_PLUGIN_MODULE = ('Forms')
DJANGOCMS_FORMS_PLUGIN_NAME = ('Form')

DJANGOCMS_FORMS_DEFAULT_TEMPLATE = 'djangocms_forms/form_template/default.html'
DJANGOCMS_FORMS_TEMPLATES = (
    ('djangocms_forms/form_template/default.html', ('Default')),
)

DJANGOCMS_FORMS_USE_HTML5_REQUIRED = False

DJANGOCMS_FORMS_WIDGET_CSS_CLASSES = {'__all__': ('form-control',)}

# CKEditor Configuration including embedded images

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

TEXT_SAVE_IMAGE_FUNCTION = 'djangocms_text_ckeditor.picture_save.create_picture_plugin'

FILER_CANONICAL_URL = 'sharing/'

CKEDITOR_UPLOAD_PATH = 'filer_public/'
CKEDITOR_THUMBNAIL_PATH = 'filer_public_thumbnails/filer_public/'
CKEDITOR_IMAGE_BACKEND = "pillow"

CMSPLUGIN_FILER_IMAGE_STYLE_CHOICES = (
    ('default', 'Default'),
    ('boxed', 'Boxed'),
)
CMSPLUGIN_FILER_IMAGE_DEFAULT_STYLE = 'boxed'

THUMBNAIL_PROCESSORS = (
    'easy_thumbnails.processors.colorspace',
    'easy_thumbnails.processors.autocrop',
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'easy_thumbnails.processors.filters',
)

THUMBNAIL_HIGH_RESOLUTION = True

CKEDITOR_BROWSE_SHOW_DIRS = True


CKEDITOR_CONFIGS = {
    'default': {
        'language': '{{ language }}',
        'mathJaxLib': '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML',
        'allowedContent': True,
        'toolbarCanCollapse': False,
        'toolbar': 'Custom',
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['cmsplugins'],
            ['-', 'ShowBlocks'],
            ['Format', 'Styles'],
            ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
            ['Mathjax', 'SpecialChar'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
            ['CreateDiv', 'SpeCaption', 'Blockquote', 'HorizontalRule'],
            ['Link', 'Unlink'],
            ['Image', 'Youtube'],
            # ['FilerImage', 'Youtube'],
            ['Source', 'Preview'],
            ['Maximize'],
        ],
        'extraPlugins': ','.join(
            [
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'mathjax',
                'maximize',
                'justify',
                'div',
                'specialchar',
                'blockquote',
                'horizontalrule',
                'image2',
                # 'filerimage',
                'youtube',
                'specaption',
            ]),
        'removePlugins': ','.join(['stylesheetparser', 'image']),
        # 'removePlugins': 'stylesheetparser',
        # 'removePlugins': 'image',
        'skin': 'moono',
        'filebrowserImageBrowseUrl': '/ckeditor/browse/?type=image',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'filebrowserUploadUrl': '',
        'contentsCss': ['/static/ckeditor/editor.css'],
        'specialChars': ','.join(
            [
                '&alpha;&beta;&gamma;&delta;&epsilon;&zeta;&eta;&theta;&iota;&kappa;&lambda;&mu;&nu;&xi;&omicron;&pi;&rho;&sigma;&sigma;&tau;&upsilon;&phi;&chi;&psi;&omega;&Delta;&euro;&lsquo;&rsquo;&ldquo;&rdquo;&ndash;&mdash;&iexcl;&cent;&pound;&curren;&yen;&brvbar;&sect;&uml;&copy;&ordf;&laquo;&not;&reg;&macr;&deg;&sup2;&sup3;&acute;&micro;&para;&middot;&cedil;&sup1;&ordm;&raquo;&frac14;&frac12;&frac34;&iquest;&Agrave;&Aacute;&Acirc;&Atilde;&Auml;&Aring;&AElig;&Ccedil;&Egrave;&Eacute;&Ecirc;&Euml;&Igrave;&Iacute;&Icirc;&Iuml;&ETH;&Ntilde;&Ograve;&Oacute;&Ocirc;&Otilde;&Ouml;&times;&Oslash;&Ugrave;&Uacute;&Ucirc;&Uuml;&Yacute;&THORN;&szlig;&agrave;&aacute;&acirc;&atilde;&auml;&aring;&aelig;&ccedil;&egrave;&eacute;&ecirc;&euml;&igrave;&iacute;&icirc;&iuml;&eth;&ntilde;&ograve;&oacute;&ocirc;&otilde;&ouml;&divide;&oslash;&ugrave;&uacute;&ucirc;&uuml;&yacute;&thorn;&yuml;&OElig;&oelig;&#372;&#374;&#373;&#375;&sbquo;&#8219;&bdquo;&hellip;&trade;&#9658;&bull;&rarr;&rArr;&hArr;&diams;&asymp;',
            ]),
    },
}


# djangocms-text-ckeditor uses CKEDITOR_SETTINGS so including here in case we use it

CKEDITOR_SETTINGS = {
    'default': {
        'language': '{{ language }}',
        'mathJaxLib': '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS_HTML',
        'toolbarCanCollapse': False,
        'toolbar': 'Custom',
        'allowedContent': True,
        'toolbar_Custom': [
            ['Undo', 'Redo'],
            ['cmsplugins'],
            ['-', 'ShowBlocks'],
            ['Format', 'Styles'],
            ['Bold', 'Italic', 'Underline', '-', 'Subscript', 'Superscript', '-', 'RemoveFormat'],
            ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
            ['TextColor', 'BGColor', '-', 'PasteText', 'PasteFromWord'],
            ['Mathjax', 'SpecialChar'],
            ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Table'],
            ['CreateDiv', 'SpeCaption', 'Blockquote', 'HorizontalRule'],
            ['Link', 'Unlink'],
            ['Image', 'Youtube'],
            # ['FilerImage', 'Youtube'],
            ['Source', 'Preview'],
            ['Maximize'],
        ],
        'extraPlugins': ','.join(
            [
                'widget',
                'lineutils',
                'clipboard',
                'dialog',
                'dialogui',
                'mathjax',
                'maximize',
                'justify',
                'div',
                'specialchar',
                'blockquote',
                'horizontalrule',
                'image2',
                # 'filerimage',
                'youtube',
                'specaption',
            ]),
        'removePlugins': ','.join(['stylesheetparser', 'image']),
        # 'removePlugins': 'stylesheetparser',
        # 'removePlugins': 'image',
        'skin': 'moono',
        'filebrowserImageBrowseUrl': '/ckeditor/browse/?type=image',
        'filebrowserBrowseUrl': '/ckeditor/browse/',
        'filebrowserUploadUrl': '',
        'contentsCss': ['/static/ckeditor/editor.css'],
        'specialChars': ','.join(
            [
                '&alpha;&beta;&gamma;&delta;&epsilon;&zeta;&eta;&theta;&iota;&kappa;&lambda;&mu;&nu;&xi;&omicron;&pi;&rho;&sigma;&sigma;&tau;&upsilon;&phi;&chi;&psi;&omega;&Delta;&euro;&lsquo;&rsquo;&ldquo;&rdquo;&ndash;&mdash;&iexcl;&cent;&pound;&curren;&yen;&brvbar;&sect;&uml;&copy;&ordf;&laquo;&not;&reg;&macr;&deg;&sup2;&sup3;&acute;&micro;&para;&middot;&cedil;&sup1;&ordm;&raquo;&frac14;&frac12;&frac34;&iquest;&Agrave;&Aacute;&Acirc;&Atilde;&Auml;&Aring;&AElig;&Ccedil;&Egrave;&Eacute;&Ecirc;&Euml;&Igrave;&Iacute;&Icirc;&Iuml;&ETH;&Ntilde;&Ograve;&Oacute;&Ocirc;&Otilde;&Ouml;&times;&Oslash;&Ugrave;&Uacute;&Ucirc;&Uuml;&Yacute;&THORN;&szlig;&agrave;&aacute;&acirc;&atilde;&auml;&aring;&aelig;&ccedil;&egrave;&eacute;&ecirc;&euml;&igrave;&iacute;&icirc;&iuml;&eth;&ntilde;&ograve;&oacute;&ocirc;&otilde;&ouml;&divide;&oslash;&ugrave;&uacute;&ucirc;&uuml;&yacute;&thorn;&yuml;&OElig;&oelig;&#372;&#374;&#373;&#375;&sbquo;&#8219;&bdquo;&hellip;&trade;&#9658;&bull;&rarr;&rArr;&hArr;&diams;&asymp;',
            ]),
    },
}


DASHING = {
    'INSTALLED_WIDGETS': ('number', 'list', 'graph', 'clock', 'weather'),
}

# check if this is still needed
DEFAULT_IP = '192.152.183.80'

# Allow deferred Publishing and Retirement of CMS Pages
CMS_SHOW_START_DATE = True
CMS_SHOW_END_DATE = True

ADMIN_SHORTCUTS = [
    {
        'title': 'Channel',
        'shortcuts': [
            {
                'url': '/',
                'open_new_window': True,
                'title': 'WWW',
            },
            {
                'url': '/jpt/jpt-main-page',
                'open_new_window': True,
                'title': 'JPT',

            },
            {
                'url': '/ogf/ogf-main-page',
                'open_new_window': True,
                'title': 'OGF',

            },
            {
                'url': '/twa/twa-main-page',
                'open_new_window': True,
                'title': 'TWA',
            },
        ]
    },
    {
        'title': 'Content',
        'shortcuts': [
            {
                'url_name': 'admin:spe_blog_articleeditor_changelist',
                'url_extra': '?published__exact=0',
                'open_new_window': True,
                'title': 'Unpublished Articles',
                'count_new': 'spe_blog.utils.count_articles',
            },
            {
                'url_name': 'admin:spe_blog_briefeditor_changelist',
                'url_extra': '?published__exact=0',
                'open_new_window': True,
                'title': 'Unpublished Briefs',
                'count_new': 'spe_blog.utils.count_briefs',
            },
            {
                'url_name': 'admin:spe_blog_articleeditor_changelist',
                'url_extra': '?publication__code=JPT',
                'open_new_window': True,
                'title': 'JPT Articles',
            },
            {
                'url_name': 'admin:spe_blog_articleeditor_changelist',
                'url_extra': '?publication__code=OGF',
                'open_new_window': True,
                'title': 'OGF Articles',
            }, {
                'url_name': 'admin:spe_blog_articleeditor_changelist',
                'url_extra': '?publication__code=TWA',
                'open_new_window': True,
                'title': 'TWA Articles',
            },
        ]
    },
    {
        'title': 'Promotions',
        'shortcuts': [
            {
                'url_name': 'admin:spe_promotions_simpleeventpromotion_changelist',
                'open_new_window': True,
                'title': 'Promotions',
            },
            {
                'url': '/staff/promotions/search/',
                'open_new_window': True,
                'title': 'Test',
            },
            {
                'url': '/staff/promotions/timeline',
                'open_new_window': True,
                'title': 'Timeline',
            },
            {
                'url': '/staff/promotions/discipline',
                'open_new_window': True,
                'title': 'Discipline',
            },
            {
                'url': '/staff/promotions/region',
                'open_new_window': True,
                'title': 'Region',
            },
            {
                'url': '/staff/promotions/event_type',
                'open_new_window': True,
                'title': 'Event Type',
            },
        ]
    },
]

ADMIN_SHORTCUTS_CLASS_MAPPINGS = [
    ['ogf', 'home'],
    ['jpt', 'home'],
    ['twa', 'home'],
    ['search', 'ok'],
    ['timeline', 'clock'],
    ['discipline', 'user'],
    ['region', 'pin'],
    ['event_type', 'date'],
]

ADMIN_SHORTCUTS_SETTINGS = {
    'hide_app_list': False,
    'open_new_window': False,
}


# Admin Dashboard

CONTROLCENTER_DASHBOARDS = (
    'mainsite.dashboards.MyDashboard',
)


# Ensure SEO Fileds are Turned on

CMS_SEO_FIELDS = True

# Django Base CACHE setup

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#         'LOCATION': 'mainsite',
#     }
# }