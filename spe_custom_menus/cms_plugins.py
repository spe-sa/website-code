from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import CustomMenuItems, CustomMenusPlugin


class CustomMenuPluginInstance(CMSPluginBase):
    model = CustomMenusPlugin
    name = "Custom Menu"
    render_template = "spe_custom_menus/menu.html"
    allow_children = True
    module = 'Components'

    def render(self, context, instance, placeholder):
        menu_items = CustomMenuItems.objects.filter(custom_menu=instance.custom_menu)
        previous_is_child = 0
        for item in reversed(menu_items):
            item.is_dropdown_node = previous_is_child
            if item.level == 2:
                previous_is_child = 1
                item.is_dropdown_node = 0
            else:
                previous_is_child = 0
        previous_is_child = 0
        for item in menu_items:
            if previous_is_child and item.level == 1:
                item.is_back_up = 1
            else:
                item.is_back_up = 0
            if item.level == 2:
                previous_is_child = 1
            else:
                previous_is_child = 0
        context.update({
            'branding': instance.custom_menu.branding,
            'link': instance.custom_menu.get_link(),
            'items': menu_items,
            })
        return context

plugin_pool.register_plugin(CustomMenuPluginInstance)
