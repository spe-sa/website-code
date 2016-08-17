from django import template

register = template.Library()


@register.filter
def tostring(value):

    value = str(value)

    return value
