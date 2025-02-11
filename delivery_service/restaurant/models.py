from django.db import models
from dish import models as dish_models


class CreatedUpdatedMixin(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
        )
    updated_at = models.DateTimeField(
        verbose_name='Дата обновления',
        auto_now=True
        )

    class Meta:
        abstract = True

class Restaurant(CreatedUpdatedMixin):
    name = models.CharField(
        verbose_name='Название',
        max_length=64,
        null=False,
        blank=False
    )
    address = models.CharField(
        verbose_name='Адрес',
        max_length=128,
        null=False,
        blank=False
        )
    contact_info = models.CharField(
        verbose_name='Контактная информация',
        max_length=64,
        null=False,
        blank=False
        )
    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True
        )
    logo = models.ImageField(
        verbose_name='Логотип',
        upload_to='restaurant_logo',
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ресторан'
        verbose_name_plural = 'Рестораны'
    

    

    
class Menu(CreatedUpdatedMixin):
    restaurant = models.OneToOneField(
        Restaurant,
        on_delete=models.CASCADE,
        verbose_name='Ресторан',
        related_name='menu'
        )
    dishes = models.ManyToManyField(
        dish_models.Dish,
        verbose_name='Блюда',
        related_name='menu'
    )

    def __str__(self):
        return f'Меню ресторана {self.restaurant.name}'
    

