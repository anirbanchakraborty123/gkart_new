# Generated by Django 3.1 on 2022-01-27 19:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0004_auto_20220128_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='cartitems',
            name='added_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
