from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import SET_NULL
from inventory.models import Company,Department

# Create your models here.



class Profile(AbstractUser):
    """"""
    email=models.EmailField(unique=True,null=False)
    createdon = models.DateTimeField(auto_now_add=True)
    company = models.ManyToManyField(Company, null=True, on_delete=SET_NULL)
    department = models.ManyToManyField(Department, null=True, on_delete=SET_NULL)
    #point = models.IntegerField(default=0)
    #certification = models.BooleanField(default=False)
    #city = models.ForeignKey(City, on_delete=SET_NULL, null=True)
    #respondent = models.ForeignKey(Respondent, on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.username
        
    class Meta:
        ordering = ['id']