from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import MenuItem, Menu


class MenuPlugin(CMSPluginBase):
    model = Menu
    name = "Menu"
    render_template = "spe_menu/menu.html"
    allow_children = True

    def render(self, context, instance, placeholder):
        menu_items = MenuItem.objects.all()
        i = 0
        previous_level = 1
        for item in menu_items:
            if item.level == 1:
                i += 1
            item.sequence = i
            if previous_level == 3 and (item.level == 1 or item.level == 2):
                item.transition = 1
            previous_level = item.level
        context.update({
            'event': instance.event,
            'items': menu_items,
            })
        return context

plugin_pool.register_plugin(MenuPlugin)
