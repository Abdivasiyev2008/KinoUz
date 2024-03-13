from django.contrib import admin
from .models import Category, Country, Language, Cartoon, CartoonComment

# Register your models here.

admin.site.register(Category)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Cartoon)
admin.site.register(CartoonComment)