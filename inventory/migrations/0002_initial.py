# Generated by Django 4.0.3 on 2022-03-03 18:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goods', '0002_initial'),
        ('inventory', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroups',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='使用者ID'),
        ),
        migrations.AddField(
            model_name='package',
            name='invoice',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='inventory.invoice', verbose_name='通關單據'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='goods_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Inventory_goods_id', to='goods.good', verbose_name='商品ID'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='goods_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, related_name='Inventory_goods_name', to='goods.good', to_field='name', verbose_name='商品名稱'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='packedin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.package', verbose_name='包裹清關條碼'),
        ),
        migrations.AddField(
            model_name='inventory',
            name='stockin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.warehouse', verbose_name='倉庫別'),
        ),
        migrations.AddField(
            model_name='company',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.country', verbose_name='註冊國家'),
        ),
    ]
