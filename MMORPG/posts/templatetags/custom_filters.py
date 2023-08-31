from django import template

register = template.Library()

# экперементировал. фильтр не пригодился, пока пусть будет тут.


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key)
