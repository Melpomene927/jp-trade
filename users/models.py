from tabnanny import verbose
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from django.utils.translation import gettext_lazy as _

# Create your models here.



class Profile(AbstractUser):
    """"""
    email=models.EmailField(unique=True,null=False)
    createdon = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        _name = f'{self.last_name}{self.first_name}' if self.first_name != "" else self.username
        return _name
        
    class Meta:
        ordering = ['id']
        verbose_name = _('使用者資訊')
