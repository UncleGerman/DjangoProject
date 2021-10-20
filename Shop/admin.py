from django.contrib import admin
from .models import Category, Product, Order, OrderItem

class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'slug')
	prepopulated_fields = {'slug': ('category_name',)}

admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
	list_display = ['product_name', 'slug', 'product_price', 
					'product_stock', 'available','active',]
	list_filter = ['available', 'active']
	list_editable = ['product_price', 'product_stock', 'available']
	prepopulated_fields = {'slug': ('product_name',)}

admin.site.register(Product, ProductAdmin)

class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'postal_code', 'city', 'paid',
                    'created', 'updated', 'user']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)