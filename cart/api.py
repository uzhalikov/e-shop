
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
import json
from .cart import Cart
from .models import Product
from django.shortcuts import get_object_or_404


@csrf_exempt
def update_cart_session(request):
    data = json.loads(request.body)
    item_id = data.get('itemId')
    item_quantity = data.get('itemQuantity')
    if item_id:
        cart = Cart(request)
        product = get_object_or_404(Product, id=int(item_id))
        cart.add(product=product, quantity=int(item_quantity), override_quantity=True)
    return JsonResponse(200, safe=False)

def cart_add(request, product_slug):
    cart = Cart(request)
    product = get_object_or_404(Product, slug=product_slug)
    cart.add(product)
    return JsonResponse(cart.cart)

def clear_cart(request):
    cart = Cart(request)
    cart.clear()
    return JsonResponse(200, safe=False)

def remove_item(request, item_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=int(item_id))
    cart.remove(product)
    return JsonResponse(200, safe=False)

def get_cart_data(request):
    cart = Cart(request)
    result = {'totalPrice': 0, 'totalQuantity': 0}
    for item in cart:
        result['totalPrice'] += item['price']
        result['totalQuantity'] += int( item['quantity'])
    return JsonResponse(result)