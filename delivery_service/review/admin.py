from django.contrib import admin
from .models import Review

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'dish', 'rating', 'comment')
    list_filter = ('author', 'dish', 'rating')
    search_fields = ('author', 'dish', 'rating')
    class Meta:
        model = Review
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

admin.site.register(Review, ReviewAdmin)
