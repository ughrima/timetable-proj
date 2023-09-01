from django import template

register = template.Library()

@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@register.filter
def get_nested_value(dictionary, keys, default=None):
    try:
        keys = keys.split('.')
        for key in keys:
            dictionary = dictionary.get(key, {})
    except AttributeError:
        dictionary = {}
    return dictionary or default
