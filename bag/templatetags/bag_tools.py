from django import template
register = template.Library()
@register.filter(name='cal_subtotal')
def cal_subtotal(price, quantity):
    """Calculate subtotal for an item in the bag."""
    return price * quantity