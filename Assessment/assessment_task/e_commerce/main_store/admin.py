from django.contrib import admin


from .models import Item, OrderedItem, Category, Cart, SubCategory, Labels


# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = (Item.get_category, "name", "price", "vendor")
    list_filter = ( "price", "vendor", 'name',)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name",'category' )
    list_filter = ("category",)



admin.site.register(Item, ItemAdmin)
admin.site.register(OrderedItem)
admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Labels)
