# Generated by Django 3.1 on 2022-02-03 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
        ('carts', '0002_auto_20220203_1711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitems',
            name='test',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='store.product'),
        ),
    ]
