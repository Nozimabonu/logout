from django.contrib import admin
from django.contrib.auth.models import Group

from blog.models import Product, Image, Attribute, Customer, AttributeValue, ProductAttribute, User

# Register your models here.


# admin.site.register(Product)
admin.site.register(Image)
admin.site.register(Attribute)
admin.site.register(Customer)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)
# admin.site.register(User)

admin.site.unregister(Group)


# admin.site.register(admin.CustomerAdmin)


@admin.register(Product)
class Product(admin.ModelAdmin):
    List_display = ("name", 'price', 'slug')
    # prepopulated_fields = {'slug': ('name',)}


@admin.register(User)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "is_superuser")
    search_fields = ('email',)
    list_filter = ('date_joined',)
