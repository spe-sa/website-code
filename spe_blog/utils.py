from .models import Article, Brief

def count_articles():
    return Article.objects.filter(published=False).count()

def count_briefs():
    return Brief.objects.filter(published=False).count()