from django import template

register = template.Library()


@register.simple_tag
def get_value_wh_item(arg1, arg2, arg3):
    return arg1[f"{arg2}{arg3}"]
