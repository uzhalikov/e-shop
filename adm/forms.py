from django import forms
from app.models import Category, Product

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug', 'created', 'updated']