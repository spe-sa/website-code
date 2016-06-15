from django.apps import AppConfig


class MainsiteConfig(AppConfig):
    name = 'mainsite'
    verbose_name = "Utility Common Lists and Information"


class FilerConfig(AppConfig):
    name = 'filer'
    verbose_name = "Files and Images"


class FilerPluginConfig(AppConfig):
    name = 'cmsplugin_filer_image'
    verbose_name = "Utility Picture Configurations"


class RequestConfig(AppConfig):
    name = 'request'
    verbose_name = "Utility Request Configurations"


class SmartsnippetConfig(AppConfig):
    name = 'smartsnippets'
    verbose_name = "Utility SmartSnippet Configurations"


class SpeBlogConfig(AppConfig):
    name = 'spe_blog'
    verbose_name = "Content"


class SpeEventConfig(AppConfig):
    name = 'spe_events'
    verbose_name = "Utility Event Lists"


class SpeLinkConfig(AppConfig):
    name = 'spe_links'
    verbose_name = "Links"


class SpePollConfig(AppConfig):
    name = 'spe_polls'
    verbose_name = "Polls"
