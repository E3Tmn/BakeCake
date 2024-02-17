from django.db import models


# Create your models here.
class Cake(models.Model):
    comment = models.CharField(
        'Комментарий',
        max_length=50,
        default='Без подписи'
    )


class Level(models.Model):
    level = models.CharField(
        'Количество уровней',
        max_length=15,
        choices=(
            ('не выбрано', 'не выбрано'),
            ('1', '1'),
            ('2', '2'),
            ('3', '3'),
        )
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.level == '1':
            self.cost = 400
        elif self.level == '2':
            self.cost = 750
        elif self.level == '3':
            self.cost = 1100
        else:
            self.cost = 0

        super(Level, self).save(*args, **kwargs)


class Form(models.Model):
    form = models.CharField(
        'Форма',
        max_length=20,
        choices=(
            ('не выбрано', 'не выбрано'),
            ('Круг', 'Круг'),
            ('Квадрат', 'Квадрат'),
            ('Прямоугольник', 'Прямоугольник'),
        ),
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.form == 'Круг':
            self.cost = 600
        elif self.form == 'Квадрат':
            self.cost = 400
        elif self.form == 'Прямоугольник':
            self.cost = 1000
        else:
            self.cost = 0

        super(Form, self).save(*args, **kwargs)


class Topping(models.Model):
    topping = models.CharField(
        'Топпинг',
        max_length=20,
        choices=(
            ('не выбрано', 'не выбрано'),
            ('Без', 'Без'),
            ('Белый соус', 'Белый соус'),
            ('Карамельный', 'Карамельный'),
            ('Кленовый', 'Кленовый'),
            ('Черничный', 'Черничный'),
            ('Молочный шоколад', 'Молочный шоколад'),
            ('Клубничный', 'Клубничный'),
        ),
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.topping == 'Белый соус':
            self.cost = 200
        elif self.topping == 'Карамельный':
            self.cost = 180
        elif self.topping == 'Кленовый':
            self.cost = 1200
        elif self.topping == 'Черничный':
            self.cost = 300
        elif self.topping == 'Молочный шоколад':
            self.cost = 350
        elif self.topping == 'Клубничный':
            self.cost = 200
        else:
            self.cost = 0

        super(Topping, self).save(*args, **kwargs)


class Berries(models.Model):
    berries = models.CharField(
        'Ягоды',
        max_length=20,
        choices=(
            ('нет', 'нет'),
            ('Ежевика', 'Ежевика'),
            ('Малина', 'Малина'),
            ('Голубика', 'Голубика'),
            ('Клубника', 'Клубника'),
        )
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.berries == 'Ежевика':
            self.cost = 400
        elif self.berries == 'Малина':
            self.cost = 300
        elif self.berries == 'Голубика':
            self.cost = 450
        elif self.berries == 'Клубника':
            self.cost = 500
        else:
            self.cost = 0

        super(Berries, self).save(*args, **kwargs)


class Decor(models.Model):
    decor = models.CharField(
        'Декор',
        max_length=20,
        choices=(
            ('нет', 'нет'),
            ('Фисташки', 'Фисташки'),
            ('Безе', 'Безе'),
            ('Фундук', 'Фундук'),
            ('Пекан', 'Пекан'),
            ('Маршмеллоу', 'Маршмеллоу'),
            ('Марципан', 'Марципан'),
        )
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.decor == 'Фисташки':
            self.cost = 300
        elif self.decor == 'Безе':
            self.cost = 400
        elif self.decor == 'Фундук':
            self.cost = 350
        elif self.decor == 'Пекан':
            self.cost = 300
        elif self.decor == 'Маршмеллоу':
            self.cost = 200
        elif self.decor == 'Марципан':
            self.cost = 280
        else:
            self.cost = 0

        super(Decor, self).save(*args, **kwargs)


class Words(models.Model):
    words = models.TextField(
        'Поздравительные слова',
        max_length=100,
        blank=True
    )
    cost = models.IntegerField(
        'Стоимость',
        default=0
    )
    cake = models.ForeignKey(
        Cake,
        verbose_name='Торт',
        on_delete=models.CASCADE
    )

    def save(self, *args, **kwargs):
        if self.words:
            self.cost = 500
        else:
            self.cost = 0

        super(Words, self).save(*args, **kwargs)
