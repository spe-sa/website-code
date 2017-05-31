from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from .models import CarouselHeader, Carousel
from .models import Jumbotron
from .models import Modal, ModalBody, ModalFooter, ModalHeader
from .models import Panel
from .models import TabHeader, Tab
from .models import SpacerPlug, SingleLinkPlug


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


class ModalPlugin(CMSPluginBase):
    model = Modal
    name = "Modal"
    module = 'Components'
    render_template = "modal/modal.html"
    allow_children = True
    child_classes = ["ModalBodyPlugin", "ModalFooterPlugin", "ModalHeaderPlugin", ]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ModalBodyPlugin(CMSPluginBase):
    model = ModalBody
    name = "Modal Body"
    module = 'Components'
    render_template = "modal/modal_body.html"
    parent_classes = ["ModalPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ModalFooterPlugin(CMSPluginBase):
    model = ModalFooter
    name = "Modal Footer"
    module = 'Components'
    render_template = "modal/modal_footer.html"
    parent_classes = ["ModalPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ModalHeaderPlugin(CMSPluginBase):
    model = ModalHeader
    name = "Modal Header"
    module = 'Components'
    render_template = "modal/modal_header.html"
    parent_classes = ["ModalPlugin"]
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


class SpacerPlugPlugin(CMSPluginBase):
    model = SpacerPlug
    name = "Spacer Plug"
    module = 'Components'
    render_template = "spacerplug/spacerplug.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class SingleLinkPlugin(CMSPluginBase):
    model = SingleLinkPlug
    name = "Single Link"
    module = 'Components'
    render_template = "basic/singlelink.html"

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(JumbotronPlugin)
plugin_pool.register_plugin(ModalPlugin)
plugin_pool.register_plugin(ModalBodyPlugin)
plugin_pool.register_plugin(ModalFooterPlugin)
plugin_pool.register_plugin(ModalHeaderPlugin)
plugin_pool.register_plugin(PanelPlugin)
plugin_pool.register_plugin(SPECarouselPlugin)
plugin_pool.register_plugin(SPECarouselHeaderPlugin)
plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(TabHeaderPlugin)
plugin_pool.register_plugin(SpacerPlugPlugin)
plugin_pool.register_plugin(SingleLinkPlugin)
