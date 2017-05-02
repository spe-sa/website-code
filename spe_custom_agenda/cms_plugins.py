import datetime
from django.utils import timezone
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import CustomAgendaItems, CustomAgendaPlugin


class CustomAgendaPluginInstance(CMSPluginBase):
    model = CustomAgendaPlugin
    name = "Custom Agenda"
    render_template = "cms_plugins/agenda.html"
    allow_children = True
    module = 'Components'

    def render(self, context, instance, placeholder):
        timezone.deactivate()
        agenda_items = CustomAgendaItems.objects.filter(custom_agenda=instance.custom_agenda).order_by('start_date', 'start_time', 'end_time')
        previous_day = datetime.date(1970,1,1)
        for item in agenda_items:
            if item.start_date != previous_day:
                item.is_new_day = True
                previous_day = item.start_date
            else:
                item.is_new_day = False
        i = 0
        for item in reversed(agenda_items):
            i += 1
            item.rowspan = i
            if item.is_new_day == True:
                i = 0
        context.update({
            'title': instance.custom_agenda.title,
            'items': agenda_items,
        })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CustomAgendaPluginInstance)
