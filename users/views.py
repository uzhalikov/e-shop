from django.shortcuts import render
from orders.models import Order

def personal(request):
    orders = Order.objects.filter(user=request.user)
    context = {
        'orders': orders,
        'title': 'Личный кабинет',
    }
    return render(request, 'users/personal.html', context)