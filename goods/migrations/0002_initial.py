# Generated by Django 4.0.2 on 2022-03-02 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Good_created_by', to=settings.AUTH_USER_MODEL, verbose_name='建檔人員'),
        ),
        migrations.AddField(
            model_name='good',
            name='modifiedby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Good_modified_by', to=settings.AUTH_USER_MODEL, verbose_name='修改人員'),
        ),
        migrations.AddField(
            model_name='good',
            name='origin',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.origin', verbose_name='產地'),
        ),
        migrations.AddField(
            model_name='good',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='goods.unit', verbose_name='計價單位'),
        ),
        migrations.AddField(
            model_name='category',
            name='terms_used',
            field=models.ManyToManyField(through='goods.CatagoryPrice', to='goods.PricingTerms', verbose_name='條款碼'),
        ),
        migrations.AddField(
            model_name='catagoryprice',
            name='catagory_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CatagoryPrice_catagory_id', to='goods.category', verbose_name='商品類別'),
        ),
        migrations.AddField(
            model_name='catagoryprice',
            name='catagory_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CatagoryPrice_catagory_name', to='goods.category', to_field='name', verbose_name='類別名稱'),
        ),
        migrations.AddField(
            model_name='catagoryprice',
            name='terms',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.pricingterms', verbose_name='收費條款'),
        ),
    ]
