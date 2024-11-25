from django.urls import path
from .views import *
from .api import update_cart_session, cart_add, clear_cart, remove_item, get_cart_data

urlpatterns = [
    path('detail/', cart_detail, name='cart_detail'),
    path('update_cart_session/', update_cart_session, name='update_cart_session'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('remove_item/<int:item_id>/', remove_item, name='remove_item'),
    path('add/<slug:product_slug>', cart_add, name='cart_add'),
    path('get_cart_data/', get_cart_data, name='get_cart_data'),
]