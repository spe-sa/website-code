from .models import SpeLink, SpeLinkCategory
from django.shortcuts import get_object_or_404, render


def index(request):
    links = SpeLink.objects.order_by('-pub_date')
    context = {'latest_link_list': links}
    return render(request, 'spe_links/index.html', context)


def detail(request, category_id):
    link_category = get_object_or_404(SpeLinkCategory, pk=category_id)
    links = SpeLink.objects.filter(category_id__exact=category_id).values()
    return render(request, 'spe_links/detail.html', {'link_category': link_category, 'links': links})
