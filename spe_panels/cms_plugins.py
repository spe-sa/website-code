from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from spe_panels.models import Panel


class PanelPlugin(CMSPluginBase):
    model = Panel
    name = "Panel"
    module = 'Components'
    render_template = "spe_panels/panel.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(PanelPlugin)
