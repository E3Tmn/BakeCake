# Generated by Django 5.0.2 on 2024-02-17 15:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcartapp', '0003_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cakes', to='foodcartapp.order', verbose_name='Заказ'),
        ),
    ]
