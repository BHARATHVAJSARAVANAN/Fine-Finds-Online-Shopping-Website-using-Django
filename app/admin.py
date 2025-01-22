from django.contrib import admin
from .models import (
    Customer,
    Product,
    Cart, OrderPlaced
)
# Register your models here.

@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "name", "city", "zipcode", "state"]


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "selling_price", "discounted_price", "description", "brand", "category", "product_image"]


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "product", "quantity"]


# @admin.register(OrderPlaced)
# class OrderPlacedModelAdmin(admin.ModelAdmin):
#     list_display = ["id", "user", "customer", "product", "quantity", "ordered_date","status"]

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "customer", "product", "quantity", "ordered_date", "status"]
    list_editable = ["status"]
    list_filter = ["status", "ordered_date"]
    search_fields = ["user__username", "customer__name", "product__title"]
    
    actions = ['mark_as_packed', 'mark_as_on_the_way', 'mark_as_delivered', 'mark_as_cancelled']

    def mark_as_packed(self, request, queryset):
        queryset.update(status='Packed')
        self.message_user(request, "Selected orders have been marked as Packed.")
    mark_as_packed.short_description = "Mark selected orders as Packed"

    def mark_as_on_the_way(self, request, queryset):
        queryset.update(status='On The Way')
        self.message_user(request, "Selected orders have been marked as On The Way.")
    mark_as_on_the_way.short_description = "Mark selected orders as On The Way"

    def mark_as_delivered(self, request, queryset):
        queryset.update(status='Delivered')
        self.message_user(request, "Selected orders have been marked as Delivered.")
    mark_as_delivered.short_description = "Mark selected orders as Delivered"

    def mark_as_cancelled(self, request, queryset):
        queryset.update(status='Cancel')
        self.message_user(request, "Selected orders have been marked as Cancelled.")
    mark_as_cancelled.short_description = "Mark selected orders as Cancelled"


