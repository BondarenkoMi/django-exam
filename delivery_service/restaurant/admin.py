from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'contact_info')
    list_filter = ('name', 'address', 'contact_info')
    search_fields = ('name', 'address', 'contact_info')
    class Meta:
        model = Restaurant
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'

admin.site.register(Restaurant, RestaurantAdmin)
