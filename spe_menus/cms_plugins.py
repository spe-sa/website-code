from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import CustomMenuItems, CustomMenusPlugin


class CustomMenuPluginInstance(CMSPluginBase):
    model = CustomMenusPlugin
    name = "Custom Menu"
    render_template = "spe_menu/menu.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        menu_items = CustomMenuItems.objects.filter(custom_menu=instance.custom_menu)
        previous_level = 1
        for item in menu_items:
            if (previous_level == 3 or previous_level == 2) and (item.level == 1 or item.level == 2):
                item.transition = 1
            previous_level = item.level
        context.update({
            'custom_menu': instance.custom_menu,
            'branding': instance.custom_menu.branding,
            'items': menu_items,
            })
        return context

plugin_pool.register_plugin(CustomMenuPluginInstance)
