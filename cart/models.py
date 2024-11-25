from django.db import models
from django.contrib.auth import get_user_model
from app.models import Product


User = get_user_model()

class CartUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'Корзина пользователя: {self.user.first_name}'

class CartItem(models.Model):
    cart = models.ForeignKey(CartUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = 'Элементы корзины'

    def __str__(self):
        return self.product.name
