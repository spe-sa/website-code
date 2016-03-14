from django.shortcuts import get_object_or_404, render
from django.utils import timezone
import sys

from .models import Article, Issue


def index(request):
    articles = Article.objects.order_by('-date')
    context = {'articles': articles}
    return render(request, 'spe_blog/index.html', context)


def detail(request, article_id):
    q = get_object_or_404(Article, pk=article_id)
    q.article_hits += 1
    q.article_last_viewed = timezone.now()
    q.save()
    return render(request, 'spe_blog/detail.html', {'article': q})


def issue(request, publication_code):
    sys.stderr.write("publication_code: " + publication_code + "\n")
    issues = Issue.objects.filter(publication__code=publication_code.upper())
    context = {'issues': issues, 'publication_code': publication_code}
    return render(request, 'spe_blog/issues.html', context)
