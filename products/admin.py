from django.contrib import admin

from .models import Product, Comment


class CommentsInLine(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ['author', 'body', 'stars', 'active', ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'active', ]

    inlines = [
        CommentsInLine,
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['product', 'author', 'body', 'stars', 'active', ]
