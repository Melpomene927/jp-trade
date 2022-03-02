# Generated by Django 4.0.2 on 2022-03-02 17:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='建檔人員'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_customer_id', to='customers.customer', verbose_name='顧客'),
        ),
        migrations.AddField(
            model_name='order',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Order_customer_name', to='customers.customer', to_field='name', verbose_name='顧客姓名'),
        ),
        migrations.AddField(
            model_name='order',
            name='delivery',
            field=models.ManyToManyField(to='customers.Delivery', verbose_name='運送資訊'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='courier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='customers.express', verbose_name='貨運公司'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='package_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.package', verbose_name='包裹'),
        ),
        migrations.AddField(
            model_name='customerlist',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerList_customer_id', to='customers.customer', verbose_name='顧客代號'),
        ),
        migrations.AddField(
            model_name='customerlist',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CustomerList_customer_name', to='customers.customer', to_field='name', verbose_name='顧客姓名'),
        ),
        migrations.AddField(
            model_name='customerlist',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.department', verbose_name='部門'),
        ),
        migrations.AddField(
            model_name='contact',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customers.customer', verbose_name='顧客'),
        ),
        migrations.AddField(
            model_name='callreport',
            name='createdby',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='建檔人員'),
        ),
        migrations.AddField(
            model_name='callreport',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CallReport_customer_id', to='customers.customer', verbose_name='顧客代號'),
        ),
        migrations.AddField(
            model_name='callreport',
            name='customer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CallReport_customer_name', to='customers.customer', to_field='name', verbose_name='顧客姓名'),
        ),
        migrations.AddField(
            model_name='callreport',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='inventory.department', verbose_name='部門'),
        ),
    ]