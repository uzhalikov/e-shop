from django.urls import path
from .api import create
from .views import OrderDetailView

urlpatterns = [
    path('create/', create, name='create'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]