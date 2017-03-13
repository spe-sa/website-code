import datetime

# from itertools import chain
# from netaddr import IPAddress

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from mainsite.common import (
    get_visitor,
)
from mainsite.models import Web_Region_Country
from mainsite.common import getRegion

from .forms import TargetedMessageForMemberForm
from .models import (
    TargetedMessage,
    TargetedMessageForMemberPlugin,
)


class ShowMessagesToMemberPlugin(CMSPluginBase):
    class Meta:
        abstract = True

    allow_children = False
    cache = False
    module = 'Member Messages'
    text_enabled = False
    model = TargetedMessageForMemberPlugin
    render_template = 'spe_messages/plugins/promotion_posts.html'
    name = "Message by Customer Classification"
    form = TargetedMessageForMemberForm

    def render(self, context, instance, placeholder):
        request = context.get('request')
        visitor = get_visitor(request)
        today = datetime.date.today()
        objects = None
        if visitor and visitor.classifications:
            objects = TargetedMessage.objects.filter(show_start_date__lte=today, show_end_date__gte=today,
                show_to__in=visitor.classifications.all())[:instance.count]
            context.update({'member': {'name': visitor.name}})
        context.update({'messages': objects})
        self.render_template = instance.template
        return context


plugin_pool.register_plugin(ShowMessagesToMemberPlugin)
