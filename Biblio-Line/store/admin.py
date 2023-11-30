from django.contrib import admin
from .models.product import Products
from .models.category import Category
from .models.customer import Customer
from .models.orders import Order
from .models.news import News


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'author', 'date_publi', 'pages',
                    'publisher', 'language', 'state'
                    ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Products, AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(News)


# username = admin  password = biblioline001