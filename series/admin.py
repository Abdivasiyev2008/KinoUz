from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Serial)
admin.site.register(Country)
admin.site.register(Language)
admin.site.register(Parts)
admin.site.register(Category)