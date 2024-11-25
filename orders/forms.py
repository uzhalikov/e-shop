from .constants import DELIVERY_CHOISES, PAYMENT_CHOISES
from django import forms

class OrderForm(forms.Form):
    payment = forms.ChoiceField(choices=PAYMENT_CHOISES, label="Способ оплаты")
    delivery = forms.ChoiceField(choices=DELIVERY_CHOISES, label="Вариант доставки")
    address = forms.CharField(max_length=255, label="Адрес доставки")


class QuickOrderForm(forms.Form):
    first_name = forms.CharField(max_length=50, label="Имя")
    last_name = forms.CharField(max_length=50, label="Фамилия")
    email = forms.EmailField(label="Электронная почта")
    phone = forms.CharField(max_length=20, label="Телефон")
    payment = forms.ChoiceField(choices=PAYMENT_CHOISES, label="Способ оплаты")
    delivery = forms.ChoiceField(choices=DELIVERY_CHOISES, label="Вариант доставки")
    address = forms.CharField(max_length=255, label="Адрес доставки")


