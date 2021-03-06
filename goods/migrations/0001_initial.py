# Generated by Django 4.0.3 on 2022-04-04 21:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatagoryPrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='收費單價')),
                ('unit', models.CharField(choices=[('KG', '公斤'), ('G', '公克'), ('L', '公升')], max_length=4, verbose_name='收費單位')),
                ('currency', models.CharField(choices=[('TWD', '新台幣'), ('JPY', '日圓'), ('USD', '美金'), ('GBP', '英鎊'), ('MYR', '馬來令吉')], default='TWD', max_length=3, verbose_name='收費幣別')),
            ],
            options={
                'verbose_name': '類別適用條碼',
                'ordering': ['catagory_name'],
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='類別名稱')),
                ('is_actived', models.BooleanField(default=True, verbose_name='是否啟用')),
            ],
            options={
                'verbose_name': '商品類別',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Element',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='成分名稱')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
            ],
            options={
                'verbose_name': '成分',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='OriginCountry',
            fields=[
                ('code', models.CharField(max_length=5, primary_key=True, serialize=False, verbose_name='國碼')),
                ('name', models.CharField(max_length=50, verbose_name='名稱')),
            ],
            options={
                'verbose_name': '生產國家',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='PricingTerms',
            fields=[
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('terms', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='條款碼')),
                ('description', models.CharField(max_length=50, verbose_name='條款說明')),
            ],
            options={
                'verbose_name': '收費條款',
                'ordering': ['terms'],
            },
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('note', models.CharField(help_text='請輸入KG, L, M...等單位記號', max_length=10, primary_key=True, serialize=False, verbose_name='單位標記')),
                ('name', models.CharField(max_length=20, verbose_name='單位名稱')),
            ],
            options={
                'verbose_name': '計價單位',
                'ordering': ['note'],
            },
        ),
        migrations.CreateModel(
            name='Origin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='地名')),
                ('country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.origincountry', verbose_name='國家')),
            ],
            options={
                'verbose_name': '產地',
                'ordering': ['country', 'name'],
            },
        ),
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdon', models.DateTimeField(auto_now_add=True, verbose_name='建檔日期')),
                ('modifiedon', models.DateTimeField(auto_now_add=True, verbose_name='修改日期')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='商品名稱')),
                ('nameJP', models.CharField(max_length=50, verbose_name='商品名稱(JP)')),
                ('nameEN', models.CharField(max_length=50, verbose_name='商品名稱(EN)')),
                ('barcode', models.CharField(max_length=50, verbose_name='條碼')),
                ('description', models.TextField(blank=True, help_text='外部說明', null=True, verbose_name='說明')),
                ('memo', models.TextField(blank=True, null=True, verbose_name='內部註記或雜記')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=19, verbose_name='標準單價')),
                ('catagory', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.category', verbose_name='類別')),
                ('composition', models.ManyToManyField(to='goods.element', verbose_name='組成成分')),
            ],
            options={
                'verbose_name': '商品',
                'ordering': ['catagory', 'createdon'],
            },
        ),
    ]
