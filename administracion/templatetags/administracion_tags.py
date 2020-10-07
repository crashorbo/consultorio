from django import template

register = template.Library()

@register.filter(name='contador')
def contador(value, page):
    aux = (page - 1)*12
    return value+aux