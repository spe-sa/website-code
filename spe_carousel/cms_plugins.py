from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from spe_carousel.models import CarouselHeader, Carousel


class SPECarouselHeaderPlugin(CMSPluginBase):
    model = CarouselHeader
    name = "Carousel Header"
    module = 'Components'
    render_template = "spe_carousel/carouselheader.html"
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
    render_template = "spe_carousel/carousel.html"
    parent_classes = ["SPECarouselHeaderPlugin"]
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({
            'instance': instance,
        })
        return context


plugin_pool.register_plugin(SPECarouselPlugin)
plugin_pool.register_plugin(SPECarouselHeaderPlugin)
