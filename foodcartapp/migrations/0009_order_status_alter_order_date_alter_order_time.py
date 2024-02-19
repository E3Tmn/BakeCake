# Generated by Django 5.0.2 on 2024-02-19 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0008_account_order_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('В доставке', 'В доставке'), ('Доставлен', 'Доставлен')], default='В доставке', max_length=25, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateField(null=True, verbose_name='Дата доставки'),
        ),
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.TimeField(null=True, verbose_name='Время доставки'),
        ),
    ]
