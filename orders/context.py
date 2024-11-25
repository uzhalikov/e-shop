#context processors
from .forms import QuickOrderForm, OrderForm

def order_form(request):
    return {'order_form': OrderForm()}

def quick_order_form(request):
    return {'quick_order_form': QuickOrderForm()}