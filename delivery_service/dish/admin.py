from django.contrib import admin
from .models import Dish

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price',)
    search_fields = ('name', 'price')
    class Meta:
        model = Dish
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'

admin.site.register(Dish, DishAdmin)