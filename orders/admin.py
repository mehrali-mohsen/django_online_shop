from django.contrib import admin
from jalali_date.admin import ModelAdminJalaliMixin

from .models import Order, OrderItem


class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0
    fields = ['order', 'product', 'quantity', 'price', ]


@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['user', 'first_name', 'last_name', 'datetime_created', 'is_paid',]

    inlines = [
        OrderItemInLine,
    ]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'product', 'quantity', 'price', ]

