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

class Cartoon(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    cartoon = models.FileField(upload_to='cartoons/video/')
    image = models.ImageField(upload_to='cartoons/images/')
    min = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class CartoonComment(models.Model):
    cartoon = models.ForeignKey(Cartoon, on_delete=models.CASCADE)    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)    
    body = models.CharField(max_length=150)
    date  = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Comment of " + str(self.user.username)
    
    class Meta:
        ordering = ['-date']