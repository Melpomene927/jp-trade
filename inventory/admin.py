from django.contrib import admin
from .models import * 

# Register your models here.
admin.site.register(Country)
admin.site.register(Company)
admin.site.register(UserGroups)
admin.site.register(Department)
admin.site.register(Warehouse)
admin.site.register(Inventory)
admin.site.register(Invoice)
admin.site.register(Package)
