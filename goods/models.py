from django.db import models
from django.db.models.deletion import SET_NULL,CASCADE

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

        
class Origin(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Element(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False)
    createdon = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Good(models.Model):
    createdon = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50, null=False)
    nameJP = models.CharField(max_length=50, null=False)
    nameEN = models.CharField(max_length=50, null=False)
    barcode = models.CharField(max_length=50)
    catagory = models.ForeignKey(Category, null=True, on_delete=SET_NULL)
    description = models.TextField(null=True, blank=True)
    composition = models.ManyToManyField(Element)

    class Meta:
        ordering = ['-createdon']
