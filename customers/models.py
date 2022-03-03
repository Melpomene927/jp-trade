from tabnanny import verbose
from django.db import models
from django.utils.translation import gettext_lazy as _
from inventory.models import Package
from users.models import Profile
from inventory.models import Department
from django.db.models.deletion import SET_NULL, CASCADE, RESTRICT
from django.utils.timezone import datetime
import uuid

# Create your models here.

class Express(models.Model):
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    name = models.CharField(_('公司名稱'), max_length=50, unique=True)

    class Meta:
        ordering = ['createdon']
        verbose_name = _('物流公司')

    def __str__(self): 
        return f'{self.name}'

class Delivery(models.Model):
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    courier = models.ForeignKey(Express, verbose_name=_('貨運公司'),  on_delete=RESTRICT)
    package_id = models.ForeignKey(Package, verbose_name=_('包裹'), null=True, on_delete=SET_NULL)
    number = models.CharField(_('貨運單號'), max_length=20)
    address = models.CharField(_('地址'), max_length=100)
    name = models.CharField(_('收件人'), max_length=20)
    display = models.CharField(_('海關收件人'), max_length=20)
    phone = models.CharField(_('聯絡手機'), max_length=20)
    phone2 = models.CharField(_('連絡電話'), max_length=20) 
    description = models.TextField(_('備註'))

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('物流清單')

    def __str__(self):
        _other = f'({self.display})' if self.display != self.name else ''
        return f'{self.name}{_other} {self.phone}'


class Customer(models.Model):
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    name = models.CharField(_('姓名'), max_length=50, unique=True, null=False)
    nameJP = models.CharField(_('姓名(日)'), max_length=50)
    nameEN = models.CharField(_('姓名(英)'), max_length=50)
    

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('客戶')

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    class ContactMedia(models.TextChoices):
        Mobile = 'Mobile', _('手機')
        Phone = 'Phone', _('市話')
        Line = 'Line', 'Line'
        WeChat = 'WeChat', _('微信')
        FB = 'FB', 'FaceBook'
        Other = 'Other', _('其他')
    person = models.ForeignKey(Customer, verbose_name=_('客戶'), null=True, on_delete=SET_NULL)
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    email = models.EmailField(_('Email'))
    media_type = models.CharField(_('聯絡方式'), max_length=20, choices=ContactMedia.choices, default=ContactMedia.Mobile)
    media_number = models.CharField(_('聯絡號碼'), max_length=50)

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('客戶聯絡簿')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class CustomerList(models.Model):
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    department = models.ForeignKey(Department, verbose_name=_('部門'), on_delete=RESTRICT)
    customer_id = models.ForeignKey(Customer, verbose_name=_('客戶代號'), on_delete=CASCADE, related_name='CustomerList_customer_id')
    customer_name = models.ForeignKey(Customer, verbose_name=_('客戶姓名'), to_field='name', on_delete=CASCADE, related_name='CustomerList_customer_name')


    class Meta:
        ordering = ['-createdon']
        verbose_name = _('部門開發客戶')

    def __str__(self):
        return f'{self.department} {self.customer_id:8d} {self.customer_name}'

class CallReport(models.Model):
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    createdby = models.ForeignKey(Profile, verbose_name=_('建檔人員'), null=True, on_delete=SET_NULL)
    department = models.ForeignKey(Department, verbose_name=_('部門'), on_delete=RESTRICT)
    customer_id = models.ForeignKey(Customer, verbose_name=_('客戶代號'), on_delete=CASCADE, related_name='CallReport_customer_id')
    customer_name = models.ForeignKey(Customer, verbose_name=_('客戶姓名'), to_field='name', on_delete=CASCADE, related_name='CallReport_customer_name')
    report = models.TextField(_('報告'))

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('客戶拜訪報告')

    def __str__(self):
        return f'{datetime.strftime(self.createdon, "%Y-%m-%d")} {self.customer_id:8d} {self.customer_name} call report'


def Get_Order_Number(date=datetime.now()):
    _date = date.strftime('%Y%m%d')
    if Order.objects.filter(order_number__startswith=_date).count() > 0:
        _last = Order.objects.filter(order_number__startswith=_date).last()
        _num = int(_last.order_number[8::]) + 1
    else:
        _num = 1
    return f'{_date}{_num:04d}'


class Order(models.Model):
    uuid = models.UUIDField(_('訂單唯一碼'), primary_key=True, default=uuid.uuid4(), editable=False)
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)
    createdby = models.ForeignKey(Profile, verbose_name=_('建檔人員'), null=True, on_delete=SET_NULL)
    order_number = models.CharField(_('訂單編號'), max_length=12, default=Get_Order_Number, unique=True)
    customer_id = models.ForeignKey(Customer, verbose_name=_('客戶'),  on_delete=CASCADE, related_name='Order_customer_id')
    customer_name = models.ForeignKey(Customer, verbose_name=_('客戶姓名'), to_field='name',  on_delete=CASCADE, related_name='Order_customer_name')
    delivery = models.ManyToManyField(Delivery, verbose_name=_('運送資訊'))

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('訂單')

    def __str__(self):
        return f'{self.order_number} {self.customer_name}'
