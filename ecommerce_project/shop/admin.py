from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Product)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "category", "brand", "group", "price",)
    list_filter = ("name", "slug", "category", "brand", "group", "price",)

    search_fields = ("name", "slug", "category", "brand", "group", "price",)

@admin.register(Category)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    list_filter = ("name", "slug",)

    search_fields = ("name", "slug",)

@admin.register(Brand)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    list_filter = ("name", "slug",)

    search_fields = ("name", "slug",)

@admin.register(Group)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    list_filter = ("name", "slug",)

    search_fields = ("name", "slug",)
