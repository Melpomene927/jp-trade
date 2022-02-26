from pdb import Restart
from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE, RESTRICT
from sqlalchemy import null
from goods.models import Good
import uuid
from django.utils.timezone import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Country(models.Model):
    """國家"""
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=3, null=False)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return f'{self.code}'

class Company(models.Model):
    """公司別"""
    name = models.CharField(_('name'), max_length=50, primary_key=True)
    createdon = models.DateTimeField(_('time created'), auto_now_add=True)
    GUI = models.CharField(_('Government Uniform Invoice number'), max_length=20, null=True)
    country = models.ForeignKey(_('country'), Country, on_delete=RESTRICT)
    address = models.CharField(_('address'), max_length=100, null=True)
    phone = models.CharField(_('phone'), max_length=20, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    """部門"""
    name = models.CharField(max_length=20, primary_key=True)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Warehouse(models.Model):
    """倉庫"""
    name = models.CharField(max_length=50, primary_key=True)
    belongTo = models.ForeignKey(Department, null=True, on_delete=SET_NULL)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'

class Inventory(models.Model):
    """庫存"""
    createdon = models.DateTimeField(auto_now_add=True)
    productId = models.ForeignKey(Good, null=False, on_delete=RESTRICT)
    cost = models.DecimalField(max_digits=19, decimal_places=2)
    quantity = models.DecimalField(max_digits=19, decimal_places=2)
    price = models.DecimalField(max_digits=19, decimal_places=2)
    stockin = models.ForeignKey(Warehouse, null=False, on_delete=RESTRICT)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Invoice(models.Model):
    number = models.CharField(max_length=16, unique=True)
    invoice_date = models.DateField()
    createdon = models.DateTimeField(auto_now_add=True)
    MAWB = models.CharField(max_length=20)
    HAWB = models.CharField(max_length=20)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return f'{self.number}'


def get_pkg_num(date=datetime.now()):
    """包裹號碼自動取號"""
    _date = date.strftime('%Y%m%d')
    if Package.objects.filter(pkg_number__startswith=_date).count() > 0:
        _last = Package.objects.filter(pkg_number__startswith=_date).last()
        _num = int(_last.pkg_number[8::]) + 1
    else:
        _num = 1
    return f'{_date}{_num:04d}'


class Package(models.Model):
    """包裹"""
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    pkg_number = models.CharField(max_length=12, default=get_pkg_num, editable=False)
    createdon = models.DateTimeField(auto_now_add=True)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()

    class Meta:
        ordering = ['-createdon']

    def __str__(self):
        return f'{self.pkg_number}'
