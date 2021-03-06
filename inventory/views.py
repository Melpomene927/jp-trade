from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def inventory_list(request):
    _params = {
        "title": _('庫存現況')
    }
    
    return render(request, "./inventory/inventory.html", _params)
    
def package(request):
    _params = {
        "title": _('出貨打包')
    }
    
    return render(request, "./inventory/package.html", _params)