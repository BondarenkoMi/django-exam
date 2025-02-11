from django.db import models
from restaurant.models import CreatedUpdatedMixin
from dish.models import Dish
from django.contrib.auth import get_user_model

User = get_user_model()

REVIEW_CHOICES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5')
)
class Review(CreatedUpdatedMixin):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор',
        related_name='reviews'
        )
    dish = models.ForeignKey(
        Dish,
        on_delete=models.CASCADE,
        verbose_name='Блюдо',
        related_name='reviews'
        )
    rating = models.IntegerField(
        choices=REVIEW_CHOICES,
        verbose_name='Оценка'
        )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
        )

    def __str__(self):
        return f'Отзыв на блюдо {self.dish.name} от {self.author.username}'