# Generated by Django 3.2.5 on 2022-07-12 02:41

from django.db import migrations
import sweetapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0004_alter_product_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=sweetapp.models.CustomDateTimeField(auto_now_add=True, null=True, verbose_name='create_time'),
        ),
    ]
