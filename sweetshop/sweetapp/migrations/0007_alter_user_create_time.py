# Generated by Django 3.2.5 on 2022-07-12 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0006_alter_product_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(null=True, verbose_name='create_time'),
        ),
    ]