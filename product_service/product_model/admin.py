from django.contrib import admin
from .models import Category
# from .models import Product
# Khi các xác thực mặc định của Django là ko đủ (max_length, blank=...,)
# thì ta cần tự custom lại. Trong đây là ta tự tạo ProductAdminForm
# from .forms import ProductAdminForm

# # Register your models here.


# class ProductAdmin(admin.ModelAdmin):
#     form = ProductAdminForm
#     # sets values for how the admin site lists your products
#     list_display = ('name', 'slug', 'urlService',)
#     list_display_links = ('name',)
#     list_per_page = 50
#     ordering = ['name']
#     search_fields = ['name']
#     # sets up slug to be generated from product name
#     # tại trang admin, Tự động convert thứ mình viết trong trường 'name' vào trường 'slug'
#     prepopulated_fields = {'slug': ('name',)}


class CategoryAdmin(admin.ModelAdmin):
    # sets up values for how admin site lists categories
    list_display = ('name', 'slug', 'urlService', 'description',)
    list_display_links = ('name',)
    list_per_page = 20
    ordering = ['name']
    search_fields = ['name',]
    # sets up slug to be generated from category name
    prepopulated_fields = {'slug': ('name',)}


# Khai báo cho mô hình và khai báo cho quản trị
# admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
