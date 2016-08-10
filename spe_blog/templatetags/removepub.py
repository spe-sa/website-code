from django import template
from spe_blog.models import Publication

register = template.Library()


@register.filter
def removepub(value):
    """
    Remove the publication code from the category string.
    """
    # Get publication list #
    publist = Publication.objects.values_list('code', flat=True).all()
    value = str(value)
    valuefix = value

    for pub in publist:
        pubcheck = pub + " :: "
        if value.startswith(pubcheck):
            valuefix = value[len(pubcheck):]

    return valuefix
