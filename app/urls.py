from django.urls import path
from .views import *

urlpatterns = [
    path('', ProductListView.as_view(), name='products'),
    path('list/<slug:category_slug>', ProductListView.as_view(), name='products_by_cart'),
    path('product/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('categories/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
]