from django import template
import bleach

register = template.Library()


@register.filter
def bleachall(value):
    """
    removes tags from the text
    """
    # value.replace("<strong>", "")
    # value.replace("</strong>", "")
    try:
        value = bleach.clean(value, tags=[], strip=True)
        return value
    except:
        pass
    return ''
