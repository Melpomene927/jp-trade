# Generated by Django 4.0.3 on 2022-03-03 18:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='公司名稱')),
                ('GUI', models.CharField(max_length=20, null=True, verbose_name='統一編號')),
                ('email', models.CharField(max_length=20, null=True, verbose_name='連絡Email')),
            ],
            options={
                'verbose_name': '註冊公司',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='國家')),
                ('code', models.CharField(max_length=3, verbose_name='ISO碼')),
            ],
            options={
                'verbose_name': '國家',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='部門名稱')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('address', models.CharField(max_length=100, null=True, verbose_name='地址')),
                ('addressJP', models.CharField(max_length=100, null=True, verbose_name='地址(日文)')),
                ('addressEN', models.CharField(max_length=100, null=True, verbose_name='地址(英文)')),
                ('phone', models.CharField(max_length=20, null=True, verbose_name='連絡電話')),
                ('FAX', models.CharField(max_length=20, null=True, verbose_name='傳真號碼')),
                ('email', models.CharField(max_length=20, null=True, verbose_name='連絡Email')),
            ],
            options={
                'verbose_name': '部門',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('cost', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='進貨價')),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='數量')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='銷貨價')),
            ],
            options={
                'verbose_name': '商品庫存',
                'ordering': ['-createdon'],
            },
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16, unique=True, verbose_name='發票號碼')),
                ('invoice_date', models.DateField(auto_now_add=True, verbose_name='發票日期')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('MAWB', models.CharField(max_length=20, verbose_name='清關條碼 (MAWB)')),
                ('HAWB', models.CharField(max_length=20, verbose_name='提單號 (HAWB)')),
                ('trade_terms', models.CharField(choices=[('FOB', 'Free On Board'), ('FCA', 'Free Carrier'), ('FAS', 'Free Alongside Ship'), ('CFR', 'Cost and Freight'), ('CIF', 'Cost, Insurance and Freight'), ('CPT', 'Carriage Paid To'), ('CIP', 'Carriage and Insurance Paid To'), ('DAF', 'Delivered At Frontier'), ('DES', 'Delivered Ex Ship'), ('DEQ', 'Delivered Ex Quay'), ('DDP', 'Delivered Duty Paid'), ('DDU', 'Delivered Duty Unpaid')], max_length=3, verbose_name='貿易條款')),
                ('payment_terms', models.CharField(choices=[('PIA', 'Payment in advance'), ('Net7', 'Payment 7 days after invoice date'), ('Net10', 'Payment 10 days after invoice date'), ('Net30', 'Payment 30 days after invoice date'), ('Net60', 'Payment 60 days after invoice date'), ('EOM', 'End of month'), ('21MFI', '21st of the month following invoice date'), ('COD', 'Cash on delivery'), ('Cash account', 'Cash account'), ('Letter of credit', 'Letter of Credit'), ('Bill of exchange', 'Bill of exchange'), ('CND', 'Cash next delivery'), ('CBS', 'Cash before shipment'), ('CIA', 'Cash in advance'), ('CWO', 'Cash with order'), ('1MD', 'Monthly credit payment of a full months supply'), ('2MD', 'Monthly credit payment of two full months supply'), ('Contra', 'Contra'), ('Stage payment', 'Stage payment')], max_length=20, verbose_name='付款條款')),
                ('flight', models.CharField(max_length=20, verbose_name='航班號碼')),
            ],
            options={
                'verbose_name': '發票(日本)',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('uuid', models.UUIDField(default=uuid.UUID('6157d87d-4f67-495d-bd25-2a13202bf923'), editable=False, primary_key=True, serialize=False, verbose_name='包裹唯一碼')),
                ('pkg_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='清關條碼 (MAWB)')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('length', models.FloatField(verbose_name='長度')),
                ('width', models.FloatField(verbose_name='寬度')),
                ('height', models.FloatField(verbose_name='高度')),
                ('weight', models.FloatField(verbose_name='重量')),
            ],
            options={
                'verbose_name': '包裹',
                'ordering': ['-createdon'],
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='倉儲名稱')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('belongTo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.department', verbose_name='從屬部門')),
            ],
            options={
                'verbose_name': '倉儲',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='UserGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔時間')),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.company', verbose_name='公司別')),
                ('department_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.department', verbose_name='部門別')),
            ],
            options={
                'verbose_name': '部門群組設定',
                'ordering': ['createdon'],
            },
        ),
    ]
