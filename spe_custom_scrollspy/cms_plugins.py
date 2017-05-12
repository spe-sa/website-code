from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import ScrollSpyHeader, ScrollSpy


class ScrollSpyHeaderPlugin(CMSPluginBase):
    model = ScrollSpyHeader
    name = "ScrollSpy Header"
    module = 'Components'
    render_template = "scrollspy/scrollspyheader.html"
    allow_children = True
    child_classes = ["ScrollSpyPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class ScrollSpyPlugin(CMSPluginBase):
    model = ScrollSpy
    name = "ScrollSpy Item"
    module = 'Components'
    render_template = "scrollspy/scrollspy.html"
    parent_classes = ["ScrollSpyHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(ScrollSpyHeaderPlugin)
plugin_pool.register_plugin(ScrollSpyPlugin)
