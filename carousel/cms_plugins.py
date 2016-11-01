from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _
from .models import CarouselModel, CarouselComponentModel


class CarouselPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = True
    cache = False
    module = _('Carousel')
    render_template = 'carousel/carousel_plugin.html'
    model = CarouselModel
    name = _("Carousel")
    child_classes = ['CarouselComponentPlugin']

    def render(self, context, instance, placeholder):
        context.update({'label': instance.label})
        context = super(CarouselPlugin, self).render(context, instance, placeholder)
        return context

class CarouselComponentPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = True
    cache = False
    module = _('Carousel')
    render_template = 'carousel/carousel_component_plugin.html'
    model = CarouselComponentModel
    name = _("Carousel Component")
    parent_classes = ['CarouselPlugin', ]
    # child_classes = [
    #     'CarouselComponentPlugin',
    #     'ShowTextPlugin',
    # ]

    def render(self, context, instance, placeholder):
        component_href = ""
        component_href_start = ""
        component_href_end = ""
        if instance.link_to:
            component_href = instance.link_to
            component_href_start = "<a href='" + instance.link_to + "'>"
            component_href_end = "</a>"
        context.update({'component_href': component_href, 'component_href_start': component_href_start, 'component_href_end': component_href_end})
        context = super(CarouselComponentPlugin, self).render(context, instance, placeholder)
        return context


plugin_pool.register_plugin(CarouselPlugin)
plugin_pool.register_plugin(CarouselComponentPlugin)
