from django import forms
from django.utils.safestring import mark_safe


class GrapesJsWidget(forms.Textarea):
    '''
    Textarea form widget with support grapesjs.
    This is widget base config grapesjs.

    '''
    template_name = "test.html"

    class Media:
        css = {
            'all': (
                'css/grapes.min.css',
                'css/grapesjs-preset-newsletter.css',
                'css/material.css',
                'css/tooltip.css',
                'css/toastr.min.css',
            )
        }
        js = [
            'js/ajaxable.min.js',
            'js/toastr.min.js',
            'js/grapes.min.js',
            'js/grapesjs-preset-newsletter.min.js'
        ]

    def get_context(self, name, value, attrs):
        context = super().get_context(name, value, attrs)
        context['widget'].update({
            'get_render_html_value': mark_safe(
                self.default_html
                ),
            })

        return context
