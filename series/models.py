from django.db import models
from accounts.models import CustomUser

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Serial(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='serial/images/')
    date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class Parts(models.Model):
    serial = models.ForeignKey(Serial, on_delete=models.CASCADE)
    part = models.CharField(max_length=150)
    part_video = models.FileField(upload_to='serial/video/')

    def __str__(self):
        return self.part
