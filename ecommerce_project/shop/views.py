from django.views.generic import ListView, CreateView, DetailView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, get_object_or_404, redirect
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group, User
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.db.models import Q
from .utils import DataMixin, menu


class HomePage(DataMixin, ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.all()


class SearchProduct(DataMixin, ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['key_item'] = self.request.GET.get('key_item')
        c_def = self.get_user_context(title='Результаты поиска')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        search_query = self.request.GET.get('key_item')
        return Product.objects.filter(Q(name__icontains=search_query) | Q(slug__icontains=search_query) | Q(
            category__slug__icontains=search_query))


class CategoriesProduct(DataMixin, ListView):
    model = Product
    template_name = 'shop/home.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category_slug'])
        c_def = self.get_user_context(title='Категория товаров')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        if self.kwargs['category_slug'] != None:
            return Product.objects.filter(category__slug=self.kwargs['category_slug'])
        else:
            return Product.objects.filter(category__slug=None)


class ProductDetail(DataMixin, ListView):
    model = Product
    template_name = 'shop/product.html'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Товары')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Product.objects.get(category__slug=self.kwargs['category_slug'], slug=self.kwargs['product_slug'])


class PaymentDelivery(DataMixin, ListView):
    model = Product
    template_name = 'shop/payment.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return dict(list(context.items()) + list(c_def.items()))


class Contacts(DataMixin, ListView):
    model = Contact
    template_name = 'shop/contacts.html'
    context_object_name = 'contacts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Контакты')
        return dict(list(context.items()) + list(c_def.items()))


def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart


def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist:
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()

    return redirect('cart_detail', )


def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id(request))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            counter += cart_item.quantity
            total += cart_item.product.price * cart_item.quantity

    except ObjectDoesNotExist:
        pass

    return render(request, 'shop/cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def cart_remove(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart_detail')


def cart_remove_product(request, product_id):
    cart = Cart.objects.get(cart_id=_cart_id(request))
    product = get_object_or_404(Product, id=product_id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart_detail')


class RegisterUser(DataMixin, CreateView):
    form_class = SignUpForm
    template_name = 'shop/signup.html'
    success_url = reverse_lazy('login')  # Перенаправление при успешной регистрации

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Регистрация')
        user_menu = menu.copy()
        user_menu.pop(3)
        user_menu.pop(4)
        c_def['menu'] = user_menu
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):  # логинит при успешной регистрации
        user = form.save()
        login(self.request, user)  # специальная функция которая авторизовывает пользователя, импорт
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'shop/login.html'


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Авторизация')
        user_menu = menu.copy()
        user_menu.pop(4)
        user_menu.pop(4)
        c_def['menu'] = user_menu
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')  # Можем заменить LOGIN_REDIRECT_URL ='/' в settings.py


def signoutView(request):
    logout(request)
    return redirect('login')
