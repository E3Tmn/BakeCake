# Generated by Django 5.0.2 on 2024-02-15 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Без подписи', max_length=50, verbose_name='Название')),
                ('comment', models.TextField(blank=True, max_length=250, verbose_name='Комментарий')),
                ('level', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=1, verbose_name='Количество уровней')),
                ('form', models.CharField(choices=[('Круг', 'Круг'), ('Квадрат', 'Квадрат'), ('Прямоугольник', 'Прямоугольник')], max_length=20, verbose_name='Форма')),
                ('topping', models.CharField(choices=[('Без', 'Без'), ('Белый соус', 'Белый соус'), ('Карамельный', 'Карамельный'), ('Кленовый', 'Кленовый'), ('Черничный', 'Черничный'), ('Молочный шоколад', 'Молочный шоколад'), ('Клубничный', 'Клубничный')], max_length=20, verbose_name='Топпинг')),
                ('berries', models.CharField(choices=[('Ежевика', 'Ежевика'), ('Малина', 'Малина'), ('Голубика', 'Голубика'), ('Клубника', 'Клубника'), ('Нет', 'Нет')], default='Нет', max_length=20, verbose_name='Ягоды')),
                ('decor', models.CharField(choices=[('Фисташки', 'Фисташки'), ('Безе', 'Безе'), ('Фундук', 'Фундук'), ('Пекан', 'Пекан'), ('Маршмеллоу', 'Маршмеллоу'), ('Марципан', 'Марципан'), ('Нет', 'Нет')], default='Нет', max_length=20, verbose_name='Декор')),
            ],
        ),
    ]
