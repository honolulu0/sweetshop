import datetime

from django.db import models
from django.forms import ModelForm
from datetime import datetime

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='user')
    password = models.CharField(max_length=128, verbose_name='password')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    is_superuser = models.BooleanField(default=False, blank=True, verbose_name='is_superuser')
    create_time = models.DateTimeField(default=datetime.now, null=True, verbose_name='create_time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = verbose_name

        db_table = 'tb_sweet_user'
        ordering = ['id']


class CustomDateTimeField(models.DateTimeField):
    def value_to_string(self, obj):
        val = self.value_from_object(obj)
        if val:
            val.replace(microsecond=0)
            return val.isoformat()
        return ''


class Product(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='product')
    price = models.CharField(max_length=25, blank=True,  null=True, verbose_name='price', editable=True)
    cost = models.CharField(max_length=25, blank=True,  null=True, verbose_name='cost')
    sales_volume = models.CharField(max_length=25, blank=True, null=True, verbose_name='sales_volume')
    amount = models.IntegerField(blank=True, null=True, verbose_name='amount')
    product_link = models.CharField(max_length=128, blank=True, null=True, verbose_name='product_link')
    profit_rate = models.CharField(max_length=128,  null=True,verbose_name='profit_rate')
    is_active = models.BooleanField(default=True, null=True,verbose_name='is_active')

    create_time = models.DateTimeField(default=datetime.now, null=True, blank=True, verbose_name='create_time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = verbose_name

        db_table = 'tb_sweet_product'
        ordering = ['id']


class Customer(models.Model):
    name = models.CharField(max_length=25, unique=True, verbose_name='customer_name')
    is_active = models.BooleanField(default=True, verbose_name='is_active')
    create_time = models.DateField(default=datetime.now, null=True, verbose_name='create_time')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'goods'
        verbose_name_plural = verbose_name

        db_table = 'tb_sweet_customer'
        ordering = ['id']
