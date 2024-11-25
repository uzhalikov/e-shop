from django import template

register = template.Library()

@register.filter
def to_str(val):
    return str(val)
    
@register.filter
def get_count(cart, val):
    return str(cart.cart[str(val)]['quantity'])