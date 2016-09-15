from django import template

register = template.Library()

@register.assignment_tag(takes_context=True)
def set_var(context, str_value):
    valstr = str_value
    start = str_value.find("{{")
    if start != -1:
        start +=2
    end = str_value.find("}}")
    if start != -1 and end != -1 and start < len(str_value):
        # attempt to get the variable from context
        # strip off everything after the first dot
        varstr = str_value[start:end]
        subvars = varstr.split(".")
        for idx, subvar in enumerate(subvars):
            if idx == 0:
                valstr = context[subvar]
            else:
                valstr = valstr.__dict__[subvar]
        #
        #
        # start = varstr.find(".")
        # if start > -1:
        #     ctxvar = varstr[:start]
        #     valstr = context[ctxvar].__dict__[varstr[start + 1:]]
        # else:
        #     valstr = context[varstr]

    return valstr