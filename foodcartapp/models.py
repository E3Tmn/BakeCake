from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Account(models.Model):
    phone = models.CharField(
        'Номер телефона',
        max_length=30
    )


class Order(models.Model):
    name = models.CharField(
        'Имя клиента',
        max_length=50
    )
    phone = PhoneNumberField(
        'Номер телефона',
        db_index=True,
        null=True
    )
    email = models.CharField(
        'Имейл',
        max_length=50,
        null=True
    )
    address = models.CharField(
        'адрес',
        max_length=100,
        null=True
    )
    date = models.DateField(
        'Дата создания заказа',
        null=True
    )
    time = models.TimeField(
        'Время создания заказа',
        null=True
    )
    delivery_comments = models.TextField(
        max_length=250,
        null=True
    )
    owner = models.ForeignKey(
        Account,
        verbose_name='Владелец',
        on_delete=models.CASCADE,
        related_name='orders',
        null=True
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

    def save(self, *args, **kwargs):
        if self.words:
            self.cost = 500
        else:
            self.cost = 0

        super(Words, self).save(*args, **kwargs)


class Cake(models.Model):
    comment = models.CharField(
        'Комментарий',
        max_length=50,
        default='Без подписи'
    )
    order = models.ForeignKey(
        Order,
        verbose_name='Заказ',
        on_delete=models.CASCADE,
        related_name='cakes',
        null=True
    )
    level = models.ForeignKey(
        Level,
        verbose_name='Уровень',
        on_delete=models.CASCADE,
        null=True
    )
    form = models.ForeignKey(
        Form,
        verbose_name='Форма',
        on_delete=models.CASCADE,
        null=True
    )
    topping = models.ForeignKey(
        Topping,
        verbose_name='Топпинг',
        on_delete=models.CASCADE,
        null=True
    )
    berries = models.ForeignKey(
        Berries,
        verbose_name='Ягоды',
        on_delete=models.CASCADE,
        null=True
    )
    decor = models.ForeignKey(
        Decor,
        verbose_name='Декор',
        on_delete=models.CASCADE,
        null=True
    )
    words = models.ForeignKey(
        Words,
        verbose_name='Слова',
        on_delete=models.CASCADE,
        null=True
    )
