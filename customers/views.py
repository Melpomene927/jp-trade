from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def customer_list(request):
    _params ={
        "title": _('顧客清單')
    }
    return render(request, "./goods/goods.html", _params)

    