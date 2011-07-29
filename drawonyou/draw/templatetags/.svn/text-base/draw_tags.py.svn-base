from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('facebook_js.html')
def facebook_js():
    return {'facebook_api_key' : settings.FACEBOOK_API_KEY,
            'facebook_canvas_url' : settings.FACEBOOK_CANVAS_URL}

@register.inclusion_tag('facebook_button.html')
def facebook_button():
    return {'facebook_extended_permissions' : settings.FACEBOOK_EXTENDED_PERMISSIONS,
            'facebook_canvas_url' : settings.FACEBOOK_CANVAS_URL}
