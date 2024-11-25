from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from app.models import Category, Product
from .forms import CategoryCreateForm, ProductCreateForm
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin


class AdminTemplateView(PermissionRequiredMixin, TemplateView):
    template_name = 'adm/adm.html'
    permission_required = 'adm.category_add'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Панель управления'
        return context
        

class CategoryCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'adm.category_add'
    model = Category
    form_class = CategoryCreateForm
    template_name = 'adm/category_add.html'
    success_url = reverse_lazy('adm')

class CategoryUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'adm.category_add'
    model = Category
    form_class = CategoryCreateForm
    template_name = 'adm/category_add.html'
    success_url = reverse_lazy('adm')

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'adm.category_add'
    model = Product
    fields = ['category', 'name', 'description', 'image', 'price']
    form = ProductCreateForm
    template_name = 'adm/product_add.html'
    success_url = reverse_lazy('adm')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'adm.category_add'
    model = Product
    template_name = 'adm/product_add.html'
    fields = ['category', 'name', 'description', 'image', 'price']
    context_object_name = 'product'
    form = ProductCreateForm
    success_url = reverse_lazy('adm')

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'adm.category_add'
    model = Product
    template_name = 'adm/product_delete.html'
    success_url = reverse_lazy('adm')
