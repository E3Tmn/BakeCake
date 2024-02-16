from django.db import models


# Create your models here.
class Cake(models.Model):
    title = models.CharField(
        'Название',
        max_length=50,
        default='Без подписи'
    )
    comment = models.TextField(
        'Комментарий',
        max_length=250,
        blank=True
    )
    level = models.CharField(
        'Количество уровней',
        max_length=1,
        choices=(
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        ),
        default='1',
    )
    form = models.CharField(
        'Форма',
        max_length=20,
        choices=(
            ('Круг', 'Круг'),
            ('Квадрат', 'Квадрат'),
            ('Прямоугольник', 'Прямоугольник'),
        ),
    )
    topping = models.CharField(
        'Топпинг',
        max_length=20,
        choices=(
            ('Без', 'Без'),
            ('Белый соус', 'Белый соус'),
            ('Карамельный', 'Карамельный'),
            ('Кленовый', 'Кленовый'),
            ('Черничный', 'Черничный'),
            ('Молочный шоколад', 'Молочный шоколад'),
            ('Клубничный', 'Клубничный'),
        ),
    )
    berries = models.CharField(
        'Ягоды',
        max_length=20,
        choices=(
            ('Ежевика', 'Ежевика'),
            ('Малина', 'Малина'),
            ('Голубика', 'Голубика'),
            ('Клубника', 'Клубника'),
            ('Нет', 'Нет'),
        ),
        default='Нет'
    )
    decor = models.CharField(
        'Декор',
        max_length=20,
        choices=(
            ('Фисташки', 'Фисташки'),
            ('Безе', 'Безе'),
            ('Фундук', 'Фундук'),
            ('Пекан', 'Пекан'),
            ('Маршмеллоу', 'Маршмеллоу'),
            ('Марципан', 'Марципан'),
            ('Нет', 'Нет'),
        ),
        default='Нет'
    )

