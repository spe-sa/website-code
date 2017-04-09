from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from spe_tabs.models import TabHeader, Tab


class TabHeaderPlugin(CMSPluginBase):
    model = TabHeader
    name = "Tabs Header"
    module = 'Components'
    render_template = "spe_tabs/tabheader.html"
    allow_children = True
    child_classes = ["TabPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context


class TabPlugin(CMSPluginBase):
    model = Tab
    name = "Tab"
    module = 'Components'
    render_template = "spe_tabs/tab.html"
    parent_classes = ["TabHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
            })
        return context


plugin_pool.register_plugin(TabPlugin)
plugin_pool.register_plugin(TabHeaderPlugin)