# Generated by Django 3.2.5 on 2022-07-12 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sweetapp', '0007_alter_user_create_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='create_time',
            field=models.DateTimeField(blank=True, null=True, verbose_name='create_time'),
        ),
    ]
