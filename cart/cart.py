from project.settings import CART_SESSION_ID
from app.models import Product
from .models import CartUser, CartItem

class Cart:
    def __init__(self, request):
        self.user = request.user        
        self.session = request.session
        self.user_cart = None
        cart = {}
        if self.user.id:
            
            self.user_cart, created = CartUser.objects.get_or_create(user=self.user)
            for item in CartItem.objects.filter(cart=self.user_cart):
                cart[str(item.product.id)] = {
                    'quantity': str(item.quantity),
                    'price': item.product.price,
                }
        else:
            cart = self.session.get(CART_SESSION_ID)
            if not cart:
                cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def save(self):
        if self.user.id:
            for product_id in self.cart:
                product = Product.objects.get(pk=int(product_id))
                cart_item = CartItem.objects.filter(cart=self.user_cart, product=product)
                if cart_item:
                    cart_item[0].quantity = self.cart[product_id]['quantity']
                    cart_item[0].save()
                else:
                    print('Сохранение в корзину', self.user_cart, product, self.cart[product_id]['quantity'])
                    CartItem.objects.create(cart=self.user_cart, product=product, quantity=self.cart[product_id]['quantity'])
        else:
            self.session.modified = True

    def add(self, product, quantity=1, override_quantity=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'price': str(product.price),
                'total_price': str(product.price),
            }
        self.cart[product_id]['total_price'] = str(int(quantity) * int(product.price))
        if override_quantity:
            self.cart[product_id]['quantity'] = quantity
            self.cart[product_id]['total_price'] = str(int(quantity) * int(product.price))
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_length(self):
        return sum(int(item['quantity']) for item in self.cart.values())

    def get_total_price(self):
        return sum(int(item['price']) * int(item['quantity']) for item in self.cart.values())

    def clear(self):
        if self.user.id:
            CartUser.objects.get(user=self.user).delete()
        else:
            del self.session[CART_SESSION_ID]
        # self.save()

    def __iter__(self):
        products_id = self.cart.keys()
        products = Product.objects.filter(id__in=products_id)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        
        for item in cart.values():
            item['price'] = int(item['price'])
            item['total_price'] = int(item['price']) * int(item['quantity'])
            yield item