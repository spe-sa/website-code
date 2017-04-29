from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CarouselHeader, Carousel
from .models import Jumbotron
from .models import Panel
from .models import TabHeader, Tab


class JumbotronPlugin(CMSPluginBase):
    model = Jumbotron
    name = "Jumbotron"
    module = 'Components'
    render_template = "jumbotron/jumbotron.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class PanelPlugin(CMSPluginBase):
    model = Panel
    name = "Panel"
    module = 'Components'
    render_template = "panel/panel.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class SPECarouselHeaderPlugin(CMSPluginBase):
    model = CarouselHeader
    name = "Carousel Header"
    module = 'Components'
    render_template = "carousel/carouselheader.html"
    allow_children = True
    child_classes = ["SPECarouselPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class SPECarouselPlugin(CMSPluginBase):
    model = Carousel
    name = "Carousel Item"
    module = 'Components'
    render_template = "carousel/carousel.html"
    parent_classes = ["SPECarouselHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class TabHeaderPlugin(CMSPluginBase):
    model = TabHeader
    name = "Tabs Header"
    module = 'Components'
    render_template = "tabs/tabheader.html"
    allow_children = True
    child_classes = ["TabPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        self.render_template = instance.type
        return context


class TabPlugin(CMSPluginBase):
    model = Tab
    name = "Tab"
    module = 'Components'
    render_template = "tabs/tab.html"
    parent_classes = ["TabHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(JumbotronPlugin)
plugin_pool.register_plugin(PanelPlugin)
plugin_pool.register_plugin(SPECarouselPlugin)
plugin_pool.register_plugin(SPECarouselHeaderPlugin)
plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(TabHeaderPlugin)
