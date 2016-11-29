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
        ip = context['request'].META.get('HTTP_X_REAL_IP', None)
        editing = False
        if context['request'].toolbar and context['request'].toolbar.edit_mode != None:
            editing = context['request'].toolbar.edit_mode

        if instance.is_tracking and instance.show_component and editing == False:
            instance.impressions += 1
            instance.save()
        component_href = ""
        if instance.link_to:
            component_href = instance.link_to
        context.update({'component_href': component_href})
        context = super(CarouselComponentPlugin, self).render(context, instance, placeholder)
        if not instance.show_component:
            self.render_plugin = False
        return context


plugin_pool.register_plugin(CarouselPlugin)
plugin_pool.register_plugin(CarouselComponentPlugin)
