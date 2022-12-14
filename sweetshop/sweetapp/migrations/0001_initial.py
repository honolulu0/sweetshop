# Generated by Django 3.2.14 on 2022-07-16 14:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='customer_name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('create_time', models.DateField(default=datetime.datetime.now, null=True, verbose_name='create_time')),
            ],
            options={
                'verbose_name': 'goods',
                'verbose_name_plural': 'goods',
                'db_table': 'tb_sweet_customer',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='product')),
                ('price', models.CharField(blank=True, max_length=25, null=True, verbose_name='price')),
                ('cost', models.CharField(blank=True, max_length=25, null=True, verbose_name='cost')),
                ('sales_volume', models.CharField(blank=True, max_length=25, null=True, verbose_name='sales_volume')),
                ('amount', models.IntegerField(blank=True, null=True, verbose_name='amount')),
                ('product_link', models.CharField(blank=True, max_length=128, null=True, verbose_name='product_link')),
                ('profit_rate', models.FloatField(max_length=128, null=True, verbose_name='profit_rate')),
                ('is_active', models.BooleanField(default=True, null=True, verbose_name='is_active')),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='create_time')),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'product',
                'db_table': 'tb_sweet_product',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='user')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('is_active', models.BooleanField(blank=True, default=True, verbose_name='is_active')),
                ('is_superuser', models.BooleanField(blank=True, default=False, verbose_name='is_superuser')),
                ('create_time', models.DateTimeField(blank=True, default=datetime.datetime.now, null=True, verbose_name='create_time')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'db_table': 'tb_sweet_user',
                'ordering': ['id'],
            },
        ),
    ]
