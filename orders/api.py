from django.http.response import JsonResponse
from .forms import QuickOrderForm, OrderForm
from .constants import PAYMENT_CHOISES, DELIVERY_CHOISES
from .models import Order, OrderItem
from users.api import register
from cart.cart import Cart
from cart.models import CartUser
from django.contrib.auth import get_user_model
from app.models import Product
User = get_user_model()


def create_order(request, form, quick):
    user = request.user
    if quick:
        user = User.objects.filter(email=form.cleaned_data['email'])
        if not user:
            user = register(request, fast_create=True)
        else:
            user = user[0]
    last_order = Order.objects.all()
    number = 1 if not last_order else int(last_order.last().number) + 1
    payment = dict(PAYMENT_CHOISES)[form.cleaned_data['payment']]
    delivery = dict(DELIVERY_CHOISES)[form.cleaned_data['delivery']]
    return Order.objects.create(user=user, payment=payment, delivery=delivery, address=form.cleaned_data['address'], number=number)



def create(request):
    quick = request.GET.get('quick', False)
    form = QuickOrderForm(request.POST) if quick else OrderForm(request.POST)
    status = 401
    if form.is_valid():
        cart = Cart(request)
        order = create_order(request, form, quick)
        [OrderItem.objects.create(order=order, product=product['product'], quantity=product['quantity'], price=int(product['price']) * int(product['quantity'])) for product in cart]
        cart.clear()
        status = 200
    return JsonResponse(status, safe=False)