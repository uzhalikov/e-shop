from django.views.generic import ListView, DetailView
from .models import Product, Category
from django.db.models import Q
from .filters import ProductFilter

class ProductListView(ListView):
    template_name = 'app/products.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = Product.objects.all()
        category_slug = self.kwargs.get('category_slug')
        category = Category.objects.all()
        if category_slug:
            category = category.filter(slug=category_slug)
        self.filterset = ProductFilter(data=self.request.GET if self.request.GET else None, queryset=queryset.filter(category__in=category))
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filterset'] = ProductFilter(data=self.request.GET)
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'app/category.html'
    context_object_name = 'categories'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'app/product_detail.html'
    context_object_name = 'product'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

class CategoryDetailView(DetailView):
    model = Category
    template_name = 'app/category_detail.html'
    context_object_name = 'category'
    slug_url_kwarg = 'slug'
    

def error403(request):
    return render(request, '403.html')