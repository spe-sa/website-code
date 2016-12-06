from django import template

register = template.Library()


@register.assignment_tag(takes_context=True)
def set_laf_includes(context, var_name):
    # look for a look and feel parameter (laf) and set the different template values accordingly
    # Ex: laf = 'www' then
    #       css_template="include_www_css.html"
    #       header_template="include_www_header.html"
    #       footer_template="include_www_footer.html"
    # NOTE: the generic_base.html looks for these context variables to do includes properly
    # SEE: /mainsite/templates/generic_base.html and /mainsite/templates/www_base.html for examples
    laf_val = context['variables'].get('laf', 'www').lower()
    if laf_val:
        prefix = "include_" + laf_val
        css_val = prefix + "_css.html"
        header_val = prefix + "_header.html"
        footer_val = prefix + "_footer.html"
        context.dicts[0]["css_template"] = css_val
        context.dicts[0]["header_template"] = header_val
        context.dicts[0]["footer_template"] = footer_val

    return ''
