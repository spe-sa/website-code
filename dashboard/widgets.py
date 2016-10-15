import datetime
from dashing.widgets import NumberWidget, ListWidget

from spe_blog.models import Article, Brief

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

class TopArticlesWidget(ListWidget):
    title = 'Top Articles'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Article.objects.order_by('-article_hits')[:20]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]

class TopBriefsWidget(ListWidget):
    title = 'Top Briefs'
    more_info = ''
    get_update_at  = ''

    def get_data(self):
        queryset = Brief.objects.order_by('-article_hits')[:20]
        return [{'label':x.title, 'value':x.article_hits} for x in queryset]

