import django_filters as filters
from .models import Product, Category
from django.forms.widgets import TextInput, CheckboxInput, NumberInput



class ProductFilter(filters.FilterSet):
    all_prices = Product.objects.values_list('price', flat=True)
    min_price = min(all_prices)
    max_price = max(all_prices)

    name = filters.CharFilter(field_name='name', lookup_expr='icontains', label='Название товара')
    description = filters.CharFilter(field_name='description', lookup_expr='icontains', label='Описание товара')
    price_gte = filters.NumberFilter(field_name='price', lookup_expr='gte', label='Минимальная цена', widget=NumberInput(attrs={'min': min_price, 'max': max_price, 'placeholder': f'от {min_price} до {max_price}'}))
    price_lte = filters.NumberFilter(field_name='price', lookup_expr='lte', label='Максимальная цена', widget=NumberInput(attrs={'min': min_price, 'max': max_price, 'placeholder': f'от {min_price} до {max_price}'}))
    available = filters.BooleanFilter(field_name='available', label='В наличии', widget=CheckboxInput(attrs={'checked': 'checked'}))

    class Meta:
        model = Product
        fields = []