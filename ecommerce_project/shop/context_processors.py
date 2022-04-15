from django.core import exceptions
from django.shortcuts import render
from .models import CartItem, Category, Cart, Product
from .views import _cart_id, cart_detail


def counter(request):
    item_count = 0
    total = 0
    if 'admin' in request.path:
        return{}
    else:
        try:
            cart = Cart.objects.filter(cart_id=_cart_id(request))
            cart_items = CartItem.objects.all().filter(cart=cart[:1])
            for cart_item in cart_items:
                item_count += cart_item.quantity
                total += cart_item.product.price * cart_item.quantity
        except Cart.DoesNotExist:
            item_count = 0
    return dict(item_count=item_count, total=total)

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links)

def tota(request):
    return


