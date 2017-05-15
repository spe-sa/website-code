from django.db.models import Count

from controlcenter import Dashboard, widgets
from spe_promotions.models import PromotionsEventClicks

class PromotionClickList(widgets.ItemList):
    model = PromotionsEventClicks
    queryset = PromotionsEventClicks.objects.order_by('-id')
    list_display = ('pk', 'promotion_title', 'promotion_type', 'time', 'ip', 'vid', 'customer_id')
    sortable = True
    title = "Most Recent Promotion Clicks (100)"
    limit_to = 100
    height = 300


class PromotionClickCounts(widgets.ItemList):
    model = PromotionsEventClicks
    queryset = PromotionsEventClicks.objects.values('promotion_title').annotate(total_clicks=Count('promotion_id')).order_by('-total_clicks')
    list_display = ('promotion_title', 'total_clicks')
    sortable = True
    title = "Click Totals by Promotion"
    limit_to = 100
    height = 300


class PromotionClicksTimeChart(widgets.LineChart):
    title = 'Clicks by Day'
    model = PromotionsEventClicks


class MyDashboard(Dashboard):
    title = 'Promotions Dashboard'
    widgets = (
        widgets.Group([PromotionClickList], width=widgets.LARGE),
        widgets.Group([PromotionClickCounts], width=widgets.LARGE),
    )


