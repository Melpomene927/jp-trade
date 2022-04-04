from django.db import models
from django.db.models.deletion import SET_NULL, CASCADE, RESTRICT
from goods.models import Good
from users.models import Profile
import uuid
from django.utils.timezone import datetime
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Country(models.Model):
    """國家"""
    name = models.CharField(_('國家'),max_length=50, null=False)
    code = models.CharField(_('ISO碼'),max_length=3, null=False)

    class Meta:
        ordering = ['code']
        verbose_name=_('國家')

    def __str__(self):
        return f'{self.code}'

class Company(models.Model):
    """註冊公司"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    name = models.CharField(_('公司名稱'), max_length=50, primary_key=True)
    GUI = models.CharField(_('統一編號'), max_length=20, null=True)
    country = models.ForeignKey(Country, verbose_name=_('註冊國家'), on_delete=RESTRICT) 
    email = models.CharField(_('連絡Email'), max_length=50, null=True)

    class Meta:
        ordering = ['name']
        verbose_name=_('註冊公司')

    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    """部門"""
    name = models.CharField(_('部門名稱'), max_length=20, primary_key=True)
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    address = models.CharField(_('地址'), max_length=100, null=True, blank=True)
    addressJP = models.CharField(_('地址(日文)'), max_length=100, null=True, blank=True)
    addressEN = models.CharField(_('地址(英文)'), max_length=100, null=True, blank=True)
    phone = models.CharField(_('連絡電話'), max_length=20, null=True, blank=True)
    FAX = models.CharField(_('傳真號碼'), max_length=20, null=True, blank=True)
    email = models.CharField(_('連絡Email'), max_length=50, null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name=_('部門')

    def __str__(self):
        return f'{self.name}'

class UserGroups(models.Model):
    company_id = models.ForeignKey(Company, verbose_name=_('公司別'), on_delete=CASCADE)
    department_id = models.ForeignKey(Department, verbose_name=_('部門別'), on_delete=CASCADE)
    user_id = models.ForeignKey(Profile, verbose_name=_('使用者ID'), on_delete=CASCADE)
    createdon = models.DateTimeField(_('建檔時間'), auto_now_add=True)

    class Meta:
        ordering = ['createdon']
        verbose_name=_('部門群組設定')

    def __str__(self):
        return f'{self.company_id} {self.department_id} {self.user_id}'

class Warehouse(models.Model):
    """倉庫"""
    name = models.CharField(_('倉儲名稱'), max_length=50, primary_key=True)
    belongTo = models.ForeignKey(Department, verbose_name=_('從屬部門'), null=True, on_delete=SET_NULL)
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name=_('倉儲')

    def __str__(self):
        return f'{self.name}'

class Invoice(models.Model):
    """日本發票"""

    class TradeTerms(models.TextChoices):
        FOB = 'FOB', _('Free On Board')
        FCA = 'FCA', _('Free Carrier')
        FAS = 'FAS', _('Free Alongside Ship')
        CFR = 'CFR', _('Cost and Freight')
        CIF = 'CIF', _('Cost, Insurance and Freight')
        CPT = 'CPT', _('Carriage Paid To')
        CIP = 'CIP', _('Carriage and Insurance Paid To')
        DAF = 'DAF', _('Delivered At Frontier')
        DES = 'DES', _('Delivered Ex Ship')
        DEQ = 'DEQ', _('Delivered Ex Quay')
        DDP = 'DDP', _('Delivered Duty Paid')
        DDU = 'DDU', _('Delivered Duty Unpaid')

    class PaymentTerms(models.TextChoices):
        PIA = 'PIA', _('Payment in advance')
        Net7 = 'Net7', _('Payment 7 days after invoice date')
        Net10 = 'Net10', _('Payment 10 days after invoice date')
        Net30 = 'Net30', _('Payment 30 days after invoice date')
        Net60 = 'Net60', _('Payment 60 days after invoice date')
        EOM = 'EOM', _('End of month')
        _21MFI = '21MFI', _('21st of the month following invoice date')
        COD = 'COD', _('Cash on delivery')
        Cash_Account = 'Cash account', _('Cash account')
        Letter_of_Credit = 'Letter of credit', _('Letter of Credit')
        Bill_of_Exchange = 'Bill of exchange', _('Bill of exchange')
        CND = 'CND', _('Cash next delivery')
        CBS = 'CBS', _('Cash before shipment')
        CIA = 'CIA', _('Cash in advance')
        CWO = 'CWO', _('Cash with order')
        _1MD = '1MD', _('Monthly credit payment of a full month''s supply')
        _2MD = '2MD', _('Monthly credit payment of two full month''s supply')
        Contra = 'Contra', _('Contra')
        Stage_payment = 'Stage payment', _('Stage payment')

    number = models.CharField(_('發票號碼'), max_length=16, unique=True)
    invoice_date = models.DateField(_('發票日期'), auto_now_add=True, editable=True)
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    MAWB = models.CharField(_('清關條碼 (MAWB)'), max_length=20, blank=True)
    HAWB = models.CharField(_('提單號 (HAWB)'), max_length=20, blank=True)
    trade_terms = models.CharField(_('貿易條款'), max_length=3,choices=TradeTerms.choices)
    payment_terms = models.CharField(_('付款條款'), max_length=20, choices=PaymentTerms.choices)
    flight = models.CharField(_('航班號碼'), max_length=20, blank=True)

    class Meta:
        ordering = ['number']
        verbose_name=_('發票(日本)')

    def __str__(self):
        return f'{self.number}'


class Package(models.Model):
    """包裹"""
    uuid = models.UUIDField(_('包裹唯一碼'), primary_key=True, default=uuid.uuid4, editable=False)
    pkg_number = models.CharField(_('清關條碼 (MAWB)'), max_length=20, blank=True, null=True)
    createdon = models.DateTimeField(_('建檔日期'),auto_now_add=True)
    length = models.FloatField(_('長度'))
    width = models.FloatField(_('寬度'))
    height = models.FloatField(_('高度'))
    weight = models.FloatField(_('重量'))
    invoice = models.ForeignKey(Invoice, verbose_name=_('通關單據'), null=True, on_delete=RESTRICT)

    class Meta:
        ordering = ['-createdon']
        verbose_name=_('包裹')

    def __str__(self):
        return f'{self.pkg_number}'


class Inventory(models.Model):
    """庫存"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    stockin = models.ForeignKey(Warehouse, verbose_name=_('倉庫別'),  on_delete=RESTRICT)
    goods_id = models.ForeignKey(Good, verbose_name=_('商品ID'),  on_delete=RESTRICT, related_name='Inventory_goods_id')
    goods_name = models.ForeignKey(Good, verbose_name=_('商品名稱'), to_field='name',  on_delete=RESTRICT, related_name='Inventory_goods_name')
    packedin = models.ForeignKey(Package, verbose_name=_('包裹清關條碼'), on_delete=RESTRICT)
    cost = models.DecimalField(_('進貨價'), max_digits=19, decimal_places=2)
    quantity = models.DecimalField(_('數量'), max_digits=19, decimal_places=2)
    price = models.DecimalField(_('銷貨價'), max_digits=19, decimal_places=2)

    class Meta:
        ordering = ['-createdon']
        verbose_name = _('商品庫存')

    def __str__(self):
        return f'{datetime.strftime(self.createdon, "%Y-%m-%d %H:%M:%S")} {self.goods_name}'
