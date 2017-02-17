# Article and Brief Sitemaps
# (by default it uses get_absolute_url so no need for location()

from django.contrib.sitemaps import Sitemap
from .models import Article, Brief

class AllArticlesSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Article.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date

class AllBriefsSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Brief.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.date