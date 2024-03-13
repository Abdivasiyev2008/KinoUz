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

class Film(models.Model):
    name = models.CharField(max_length=150)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    # film = models.FileField(upload_to='films/video/')
    film = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='films/images/')
    min = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date']

class Comment(models.Model):
    film = models.ForeignKey(Film, on_delete=models.CASCADE)    
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)    
    body = models.CharField(max_length=150)
    date  = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return "Comment of " + str(self.user.username)
    
    class Meta:
        ordering = ['-date']