import datetime
#from cms.models import CMSPlugin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import Promotion, PromotionListingPlugin

class ShowPromotionListingPlugin(CMSPluginBase):
    class Meta:
        abstract = True
    allow_children = False
    cache = False
    module = ('Advertising')
    render_template = 'spe_blog/plugins/image_left.html'
    text_enabled = False
    model = PromotionListingPlugin
    name = ("Promotion Listing")

    def render(self, context, instance, placeholder):
        today = datetime.date.today()
        objects = Promotion.objects.filter(start__lte=today, end__gte=today).order_by('last_impression')
        
        if instance.promotion_type:
            objects = objects.filter(promotion_type=instance.promotion_type)
        if instance.disciplines.all():
            objects = objects.filter(disciplines__in=instance.disciplines.all())
        if instance.regions.all():
            objects = objects.filter(regions__in=instance.regions.all())

        objects = objects[:instance.count]

        for x in objects:
            x.url = "/promotion/" + str(x.id) + "/"
            x.impressions += 1
            x.save()
        
        context.update({'articles': objects})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(ShowPromotionListingPlugin)
