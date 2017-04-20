from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from spe_accordion.models import AccordionHeader, Accordion


class AccordionHeaderPlugin(CMSPluginBase):
    model = AccordionHeader
    name = "Accordion Header"
    module = 'Components'
    render_template = "spe_accordion/accordionheader.html"
    allow_children = True
    child_classes = ["AccordionPlugin"]

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


class AccordionPlugin(CMSPluginBase):
    model = Accordion
    name = "Accordion"
    module = 'Components'
    render_template = "spe_accordion/accordion.html"
    parent_classes = ["AccordionHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(AccordionPlugin)
plugin_pool.register_plugin(AccordionHeaderPlugin)
