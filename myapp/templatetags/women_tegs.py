from django import template
from myapp.models import *

register = template.Library()


@register.simple_tag(name='getcat')
def get_categories(filter=None):
    if not filter:
        return Categories.objects.all()
    else:
        return Categories.objects.filter(pk=filter)


@register.inclusion_tag('myapp/tags/list_categories.html')
def show_categories(sort=None,cat_selected=0):
    if not sort:
        cats = Categories.objects.all()
    else:
        cats= Categories.objects.order_by(sort)
    # cats = Categories.objects.all()
    return {'cats': cats, "cat_selected":cat_selected}
