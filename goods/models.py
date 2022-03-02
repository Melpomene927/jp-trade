from django.db import models 
from django.db.models.deletion import SET_NULL, CASCADE, RESTRICT
from django.utils.translation import gettext_lazy as _
from users.models import Profile

# Create your models here.


class PricingTerms(models.Model):
    """收費條款"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    terms = models.CharField(_('條款碼'), max_length=10, primary_key=True)
    description = models.CharField(_('條款說明'), max_length=50)

    class Meta:
        ordering = ['terms']
        verbose_name = _('收費條款')

    def __str__(self):
        return f'{self.terms}'

class Category(models.Model):
    """商品類別"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    name = models.CharField(_('類別名稱'), max_length=50, unique=True, null=False)
    is_actived = models.BooleanField(_('是否啟用'), default=True)
    terms_used = models.ManyToManyField(PricingTerms, 
        verbose_name=_('條款碼'),
        through='CatagoryPrice', 
        through_fields=['catagory_id','terms'],
        )

    class Meta:
        ordering = ['name']
        verbose_name = _('商品類別')

    def __str__(self):
        _deactived = f"({_('已停用')})" if self.is_actived == False else ''
        return f'{self.name}{_deactived}'

class CatagoryPrice(models.Model):
    """商品類別適用條碼"""
    class Unit(models.TextChoices):
        KG = 'KG', _('公斤')
        G = 'G', _('公克')
        L = 'L', _('公升')

    class Currency(models.TextChoices):
        TWD = 'TWD', _('新台幣')
        JPY = 'JPY', _('日圓')
        USD = 'USD', _('美金')
        GBP = 'GBP', _('英鎊')
        MYR = 'MYR', _('馬來令吉')

    catagory_id = models.ForeignKey(Category, verbose_name=_('商品類別'), on_delete=CASCADE, related_name='CatagoryPrice_catagory_id')
    catagory_name = models.ForeignKey(Category, verbose_name=_('類別名稱'), to_field='name', on_delete=CASCADE, related_name='CatagoryPrice_catagory_name')
    terms = models.ForeignKey(PricingTerms, verbose_name=_('收費條款'), on_delete=CASCADE)
    price = models.DecimalField(_('收費單價'), max_digits=19, decimal_places=2)
    unit = models.CharField(_('收費單位'), max_length=4, choices=Unit.choices)
    currency = models.CharField(_('收費幣別'), max_length=3, choices=Currency.choices, default=Currency.TWD)
    
    class Meta:
        ordering = ['catagory_name']
        verbose_name = _('類別適用條碼')

    def __str__(self): 
        return f'({self.terms}) {self.catagory_name}: ${self.price:0,.2f}{self.currency}/{self.unit}'.replace('$-', '-$')

class OriginCountry(models.Model):
    code = models.CharField(_('國碼'), max_length=5, primary_key=True)
    name = models.CharField(_('名稱'), max_length=50)
    class Meta:
        ordering = ['code']
        verbose_name = _('生產國家')
    
    def __str__(self) -> str:
        return f'{self.code} {self.name}'
        
class Origin(models.Model):
    """商品產地"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    country = models.ForeignKey(OriginCountry, verbose_name=_('國家'), null=True , on_delete=SET_NULL)
    name = models.CharField(_('地名'), max_length=50, unique=True)

    class Meta:
        ordering = ['country', 'name']
        verbose_name = _('產地')

    def __str__(self):
        return f'{self.country} {self.name}'

class Element(models.Model):
    """組成成分"""
    name = models.CharField(_('成分名稱'),max_length=50, unique=True, null=False)
    createdon = models.DateTimeField(_('建檔日期'),auto_now_add=True)

    class Meta:
        ordering = ['name']
        verbose_name = _('成分')

    def __str__(self):
        return self.name

class Unit(models.Model):
    """計價單位"""
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    note = models.CharField(_('單位標記'), help_text=_('請輸入KG, L, M...等單位記號'),max_length=10, primary_key=True)
    name = models.CharField(_('單位名稱'),max_length=20)

    class Meta:
        ordering = ['note']
        verbose_name = _('計價單位')

    def __str__(self):
        return f'{self.note} {self.name}'


class Good(models.Model):
    createdon = models.DateTimeField(_('建檔日期'), auto_now_add=True)
    createdby = models.ForeignKey(Profile, verbose_name=('建檔人員'), null=True, on_delete=SET_NULL, related_name='Good_created_by')
    modifiedon = models.DateTimeField(_('修改日期'), auto_now_add=True)
    modifiedby = models.ForeignKey(Profile, verbose_name=('修改人員'), null=True, on_delete=SET_NULL, related_name='Good_modified_by')
    name = models.CharField(_('商品名稱'), unique=True, max_length=50)
    nameJP = models.CharField(_('商品名稱(JP)'), max_length=50)
    nameEN = models.CharField(_('商品名稱(EN)'), max_length=50)
    barcode = models.CharField(_('條碼'), max_length=50)
    catagory = models.ForeignKey(Category, verbose_name=_('類別'), null=True, on_delete=SET_NULL)
    origin = models.ForeignKey(Origin, verbose_name=_('產地'), null=True, on_delete=SET_NULL)
    description = models.TextField(_('說明'),help_text=_('外部說明'), blank=True)
    memo = models.TextField(_('內部註記或雜記'), blank=True)
    composition = models.ManyToManyField(Element, verbose_name=_('組成成分'))
    unit_price = models.DecimalField(_('標準單價'), max_digits=19, decimal_places=2)
    unit = models.ForeignKey(Unit, verbose_name=('計價單位'), on_delete=RESTRICT)

    class Meta:
        ordering = ['catagory','createdon']
        verbose_name = _('商品')

    def __str__(self):
        return f'({self.catagory}){self.name}'
