from django.db import models
from django.shortcuts import reverse

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50,blank=False,null=False)
    phone = models.CharField(max_length=12,blank=False,null=False)
    text = models.TextField(max_length=500,blank=True,null=True)
    emergency = models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('index')

class Plasma(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    phone = models.CharField(max_length=12,blank=False,null=False)
    bloodgroup = models.CharField(max_length=10,blank=False,null=False)
    donated = models.BooleanField(default=False)
    last_donated_on = models.DateTimeField(auto_now=False)
    created_at = models.DateTimeField(default=False)

    def get_absolute_url(self):
        return reverse('index')

class Ambulance(models.Model):
    name = models.CharField(max_length=200,blank=False,null=False)
    organization = models.CharField(max_length=200,blank=True,null=True)
    phone = models.CharField(max_length=15,blank=False,null=False)
    paid= models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} {self.organization} {self.phone}'
