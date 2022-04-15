from django.urls import path
from .views import *


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('search/', SearchProduct.as_view(), name='search'),
    path('category/<slug:category_slug>/', CategoriesProduct.as_view(), name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>', ProductDetail.as_view(), name='products_detail'),
    path('cart', cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>', add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>', cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', cart_remove_product, name='cart_remove_product'),
    path('account/create/', RegisterUser.as_view(), name='signup'),
    path('account/login/', LoginUser.as_view(), name='login'),
    path('account/signout/', signoutView, name='signout'),
    path('contacts/', Contacts.as_view(), name='contacts'),
    path('payment/', PaymentDelivery.as_view(), name='payment'),
    ]