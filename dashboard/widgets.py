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
