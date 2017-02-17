from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from .models import AdSpeedZonePlugin
from .models import TitleBarPlugin
from .models import TextPlugin
# from .models import TextWithClass
from .models import TileImgBack, MarketoFormPlugin, MarketoFormPluginNoThankYou


class ShowAdSpeedZonePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Advertising')
    render_template = 'plugins/adspeed_zone_plugin.html'
    text_enabled = False
    model = AdSpeedZonePlugin
    name = _("AdSpeed Ad")

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context


class ShowTitlePlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Components')
    render_template = 'plugins/title_plugin.html'
    text_enabled = False
    model = TitleBarPlugin
    name = _("Title Bar")

    def render(self, context, instance, placeholder):
        context.update({'title': instance.title})
        context.update({'backcol': instance.backcol})
        context.update({'textcol': instance.textcol})
        return context


class ShowTextPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Components')
    render_template = 'plugins/text_plugin.html'
    text_enabled = False
    model = TextPlugin
    name = _("Text")

    def render(self, context, instance, placeholder):
        context.update({'class': instance.cls})
        context.update({'text': instance.txt})
        return context


# class ShowTextWithClassPlugin(CMSPluginBase):
#     class Meta:
#         abstract = True
#
#     allow_children = False
#     cache = True
#     module = _('Components')
#     render_template = 'plugins/text_with_class_plugin.html'
#     text_enabled = False
#     model = TextWithClass
#     name = _("Text with Class")
#
#     def render(self, context, instance, placeholder):
#         context.update({'class': instance.cls})
#         context.update({'text': instance.txt})
#         return context


class ShowTileImgBack(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = True
    module = _('Components')
    render_template = 'plugins/tile_img_back.html'
    text_enabled = False
    model = TileImgBack
    name = _("Box with Image Background")

    def render(self, context, instance, placeholder):
        context.update({'title': instance.ttl})
        context.update({'text': instance.txt})
        context.update({'image': instance.img})
        context.update({'link': instance.get_absolute_url()})
        context.update({'date': instance.date})
        context.update({'linktarget': instance.linktarget})
        return context


class ShowMarketoFormPlugin(CMSPluginBase):
    model = MarketoFormPlugin
    allow_children = False
    cache = False
    module = _('Forms')
    name = _('Marketo Form with Confirmation')
    text_enabled = False
    render_template = 'plugins/marketo_form.html'

    def render(self, context, instance, placeholder):
        context.update({'instructions': instance.instructions})
        context.update({'marketo_form': instance.marketo_form})
        context.update({'thank_you': instance.thank_you})
        return context


class ShowMarketoFormWithoutThankYouPlugin(CMSPluginBase):
    model = MarketoFormPluginNoThankYou
    allow_children = False
    cache = False
    module = _('Forms')
    name = _('Marketo Form without Confirmation')
    text_enabled = False
    render_template = 'plugins/marketo_form_no_thank_you.html'

    def render(self, context, instance, placeholder):
        context.update({'instructions': instance.instructions})
        context.update({'marketo_form': instance.marketo_form})
        return context


class ShowHorizontalBar(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = _('Components')
    name = _('Horizontal Bar')
    text_enabled = False
    render_template = 'plugins/horizontal_bar.html'

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context

plugin_pool.register_plugin(ShowMarketoFormPlugin)
plugin_pool.register_plugin(ShowMarketoFormWithoutThankYouPlugin)
plugin_pool.register_plugin(ShowAdSpeedZonePlugin)
plugin_pool.register_plugin(ShowTitlePlugin)
plugin_pool.register_plugin(ShowTextPlugin)
# plugin_pool.register_plugin(ShowTextWithClassPlugin)
plugin_pool.register_plugin(ShowTileImgBack)
plugin_pool.register_plugin(ShowHorizontalBar)
