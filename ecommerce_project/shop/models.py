from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


    def get_url(self):
        return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='brand', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'бренд'
        verbose_name_plural = 'бренды'


    def get_url(self):
        return reverse('products_by_brand', args=[self.slug])


    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='group', blank=True)


    class Meta:
        ordering = ('name',)
        verbose_name = 'группа'
        verbose_name_plural = 'группы'


    def get_url(self):
        return reverse('products_by_group', args=[self.slug])


    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250, unique=True)
    slug = models.CharField(max_length=250, unique=True)
    id_product = models.CharField(max_length=250, unique=True)
    volume = models.IntegerField()
    description = models.TextField(blank=True, default='Мы работаем над этим')
    composition = models.TextField(blank=True, default='Мы работаем над этим')
    mode_of_application = models.TextField(blank=True, default='Мы работаем над этим')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product', blank=False)
    image_1 = models.ImageField(upload_to='product_1', blank=True)
    image_2 = models.ImageField(upload_to='product_2', blank=True)
    image_3 = models.ImageField(upload_to='product_3', blank=True)
    image_4 = models.ImageField(upload_to='product_4', blank=True)
    stock = models.IntegerField()
    available = models.BooleanField(default=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_url(self):
        return reverse('products_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.name


class Cart(models.Model):
    cart_id = models.CharField(max_length=250, blank=True)
    date_added = models.DateField(auto_now_add=True)
    
    class Meta:
        ordering = ['date_added']
        db_table = 'Cart'

    def __str__(self):
        return self.cart_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    active = models.BooleanField(default=True)

    
    class Meta:
        db_table = 'CartItem'


    def sub_total(self):
        return self.product.price * self.quantity


    def __str__(self):
        return self.product


class Contact(models.Model):
    contact_name = models.CharField(max_length=30, verbose_name='Контакт')
    value = models.CharField(max_length=300, blank=True, verbose_name='Данные')
    link = models.CharField(max_length=300, blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.contact_name

    class Meta:
        # ordering = ('-price',)
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"