from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import BootStrapContainer
from .models import BootstrapRow
from .models import BootstrapColumn


class BootStrapContainerPlugin(CMSPluginBase):
    allow_children = True
    # child_classes = ['CustomRowPlugin']
    model = BootStrapContainer
    module = "Components"
    name = "Bootstrap Container"
    render_template = "cmsplugin_bootstrap_columns/container.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context


class BootstrapRowPlugin(CMSPluginBase):
    allow_children = True
    child_classes = ['BootstrapColumnPlugin']
    model = BootstrapRow
    module = "Components"
    name = "Bootstrap Row"
    render_template = "cmsplugin_bootstrap_columns/row.html"

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        return context



class BootstrapColumnPlugin(CMSPluginBase):
    allow_children = True
    fieldsets = (
        (None, {
            'fields': ('title', 'bkg_color', 'transparent', 'element_style', 'element_id',
                       'mobile_device_width', 'small_device_width',
                       'medium_device_width', 'large_device_width')
        }),
        ('Hide on Viewport Size ', {
            'classes': ('collapse',),
            'fields': ('hide_on_mobile', 'hide_on_small', 'hide_on_medium',
                       'hide_on_large')
        }),
        ('Viewport Offset', {
            'classes': ('collapse',),
            'fields': ('mobile_device_offset', 'small_device_offset',
                       'medium_device_offset', 'large_device_offset')
        }),
        ('Viewport Pull', {
            'classes': ('collapse',),
            'fields': ('mobile_device_pull', 'small_device_pull',
                       'medium_device_pull', 'large_device_pull')
        }),
        ('Viewport Push', {
            'classes': ('collapse',),
            'fields': ('mobile_device_push', 'small_device_push',
                       'medium_device_push', 'large_device_push')
        }),
    )
    model = BootstrapColumn
    module = "Components"
    name = "Bootstrap Column"
    render_template = "cmsplugin_bootstrap_columns/column.html"
    require_parent = True

    # parent_classes = ['CustomRowPlugin', 'CustomColumnPlugin']

    def render(self, context, instance, placeholder):
        context['instance'] = instance
        context['placeholder'] = placeholder
        return context


plugin_pool.register_plugin(BootStrapContainerPlugin)
plugin_pool.register_plugin(BootstrapRowPlugin)
plugin_pool.register_plugin(BootstrapColumnPlugin)
