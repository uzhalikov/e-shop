from .models import Order, OrderItem
from django.views.generic import DetailView


class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/order.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = kwargs["object"].order_items.all()
        context['title'] = f'Подробная информация по заказу {kwargs["object"]}'
        return context