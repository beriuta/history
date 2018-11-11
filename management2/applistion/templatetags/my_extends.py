"""
这是一些自定的filter或者tags
"""
from django import template

register = template.Library()


@register.simple_tag()
def sss(arg1,arg2):
    return arg1 + arg2


@register.inclusion_tag(filename='xx.html')
def my_page(num):
    date = [i for i in range(1, num + 1)]
    return {'date': date}
