from django import template
from django.forms import Media

register = template.Library()


@register.simple_tag()
def cms_media(use_jquery=True):
    js = [
        "riso-cms/utils.js",
        "riso-cms/event-handler.js",
        "riso-cms/drawer.js",
        "riso-cms/plugins.bundle.js",
        "riso-cms/custom.js",
    ]
    css = {"all": ["riso-cms/style.bundle.css", "riso-cms/custom.css", "riso-cms/plugins.bundle.css"]}
    if use_jquery:
        js.insert(0, "jquery/jquery.min.js")
    return Media(js=js, css=css)
