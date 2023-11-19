from django.contrib import admin
from api.models import Items
# Register your models here.
class Item_admin(admin.ModelAdmin):
   list_display = ('item_name', 'id', 'price', 'image')

admin.site.register(Items, Item_admin)