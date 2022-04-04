# Generated by Django 4.0.3 on 2022-04-04 19:14


from django.db import migrations
from django.db.models import Q

def create_default_company(apps, schema_editor):
    Company = apps.get_model('inventory', 'Company')
    Country = apps.get_model('inventory', 'Country')
    _jpn = Country.objects.filter(code='JPN') 
    _company = Company.objects.create(name='株式会社光のハウス', email='service@hikarinohouse.com', country=_jpn[0])
    _company.save()

def reverse_create_default_company(apps, schema_editor):
    Company = apps.get_model('inventory', 'Company')
    for _company in Company.objects.filter(id=1):
         _company.delete()

class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0003_create_default_country'),
    ]

    operations = [
        migrations.RunPython(
            create_default_company,
            reverse_create_default_company
        ),
    ]
