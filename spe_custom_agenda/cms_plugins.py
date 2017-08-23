import datetime
from django.utils import timezone
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from .models import CustomAgendaItems, CustomAgendaPlugin, SessionTypes


class CustomAgendaPluginInstance(CMSPluginBase):
    model = CustomAgendaPlugin
    name = "Custom Agenda"
    render_template = "cms_plugins/agenda.html"
    allow_children = True
    module = 'Components'

    def render(self, context, instance, placeholder):
        timezone.deactivate()
        agenda_items = CustomAgendaItems.objects.filter(custom_agenda=instance.custom_agenda).order_by('start_date',
                                                                                                       'start_time',
                                                                                                       'end_time')
        context.update({
            'title': instance.custom_agenda.title,
            'items': agenda_items,
        })
        session_css = ""
        for session_type in SessionTypes.objects.all():
            session_css += "button." + session_type.slug + "{background-color:" + session_type.bkg_color + ";color:" + session_type.text_color + ";} "
        context.update({
            'button_colors': session_css,
            'instance': instance,
        })
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(CustomAgendaPluginInstance)
