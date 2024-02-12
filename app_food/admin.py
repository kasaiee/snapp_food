from django.contrib import admin
from app_food.models import Food, Restaurant


class FoodAdmin(admin.ModelAdmin):
    list_display = ['title', 'restaurant', 'price', 'discount']
    search_fields = ['title']
    list_filter = ['restaurant']
    list_editable = ['price', 'discount']


admin.site.register(Food, FoodAdmin)
admin.site.register(Restaurant)