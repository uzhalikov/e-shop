from django.db import models
from django.contrib.auth import get_user_model
from cart.models import Product

User = get_user_model()

class Order(models.Model):
    number = models.CharField(max_length=250, verbose_name='Номер заказа')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    state = models.CharField(default='В обработке', max_length=50, verbose_name='Статус')
    payment = models.CharField(default='Карта', max_length=50, verbose_name='Способ оплаты')
    delivery = models.CharField(default='Самовывоз', max_length=50, verbose_name='Способ доставки')
    address = models.TextField(null=True, blank=True, verbose_name='Адрес доставки')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"order_{self.number}"

    class Meta:
        verbose_name_plural = 'Заказы'
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def get_total_sum(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f"{self.order} - {self.product.name}"

    class Meta:
        verbose_name_plural = 'Позиции заказов'