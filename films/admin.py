from django.contrib import admin
from .models import Category, Country, Language, Film, Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Film)
admin.site.register(Comment)