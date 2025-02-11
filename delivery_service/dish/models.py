from django.db import models


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

class Dish(CreatedUpdatedMixin):
    name = models.CharField(
        verbose_name='Название',
        max_length=64,
        blank=False,
        null=False
        )
    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=8,
        decimal_places=2,
        blank=False,
        null=False
        )
    description = models.TextField(
        verbose_name='Описание',
        blank=True,
        null=True
        )
    image = models.ImageField(
        verbose_name='Фото',
        upload_to='dish_images',
        blank=True,
        null=True
        )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
    

    