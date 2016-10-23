import datetime
from dashing.widgets import NumberWidget, ListWidget
from django.db.models import Sum

from spe_blog.models import Article, Brief
from spe_promotions.models import SimpleEventPromotion

class ArticleCountWidget(NumberWidget):
    title = 'Articles'

    def get_value(self):
        return Article.objects.all().count()

    def get_detail(self):
        count = Article.objects.filter(published=True).count()
        return '{} Published'.format(count)

    def get_more_info(self):
        count = Article.objects.filter(published=False).count()
        return '{} Un-Published'.format(count)

class BriefCountWidget(NumberWidget):
    title = 'Briefs'

    def get_value(self):
        return Brief.objects.all().count()

    def get_detail(self):
        count = Brief.objects.filter(published=True).count()
        return '{} Published'.format(count)

    def get_more_info(self):
        count = Brief.objects.filter(published=False).count()
        return '{} Un-Published'.format(count)

class PromotionCountWidget(NumberWidget):
    title = 'Active Promotions'

    def get_value(self):
        today = datetime.date.today()
        return SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).count()

    def get_detail(self):
        today = datetime.date.today()
        clicks = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).aggregate(sum=Sum('hits'))['sum']
        return '{} Clicks'.format(clicks)

    def get_more_info(self):
        today = datetime.date.today()
        impressions = SimpleEventPromotion.objects.filter(start__lte=today, end__gte=today).aggregate(sum=Sum('impressions'))['sum']
        return '{} Impressions'.format(impressions)


class TopFiveArticlesWidget(ListWidget):
    title = 'Top Five Articles'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Article.objects.order_by('-article_hits')[:5]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]

class TopTwentyArticlesWidget(ListWidget):
    title = 'Top Twenty Articles'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Article.objects.order_by('-article_hits')[:20]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]

class TopFiveBriefsWidget(ListWidget):
    title = 'Top Five Briefs'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Brief.objects.order_by('-article_hits')[:5]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]

class TopTwentyBriefsWidget(ListWidget):
    title = 'Top Twenty Briefs'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Brief.objects.order_by('-article_hits')[:20]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]
