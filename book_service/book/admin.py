from django.contrib import admin

from .models import Book, Author, Publisher

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    # sets values for how the admin site lists your products
    list_display = ('name', 'slug', 'description', 'price', 'quantity',)
    list_display_links = ('name', 'slug',)
    list_per_page = 50
    ordering = ['name']
    search_fields = ['name']
    # sets up slug to be generated from product name
    # tại trang admin, Tự động convert thứ mình viết trong trường 'name' vào trường 'slug'
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Publisher)

