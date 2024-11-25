from django.urls import path
from .api import register, login, logout
from .views import personal

urlpatterns = [
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('login/', login, name='login'),
    path('personal/', personal, name='personal'),
]
