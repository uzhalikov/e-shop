from django.urls import path
from .views import *

urlpatterns = [
    path('', AdminTemplateView.as_view(), name='adm'),
    path('product/add/', ProductCreateView.as_view(), name='product_add'),
    path('product/update/<slug:slug>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<slug:slug>/', ProductDeleteView.as_view(), name='product_delete'),
    path('category/add/', CategoryCreateView.as_view(), name='category_add'),
]