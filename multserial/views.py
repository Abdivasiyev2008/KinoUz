from django.shortcuts import render, redirect
from .models import MultSerial, Parts, Category
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.


def allseries(request):
    series = MultSerial.objects.all()
    categories = Category.objects.all()
    random_serial = np.random.choice(series, size=1, replace=False)
    random_series = np.random.choice(series, size=1, replace=False)
    context = {
        'random_serial': random_serial,
        'random_series': random_series,
        'series': series,
        'categories': categories,
    }
    return render(request, 'multserial/list.html', context)

class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)

        series = MultSerial.objects.filter(category=category)

        q=request.GET.get('q', '')

        if q:
            series = series.filter(name__icontains=q)

        return render(request, "multserial/category.html", {'series':series, "category":category, })


def SerialDetailView(request, pk):
    serial = MultSerial.objects.filter(id=pk)
    first = Parts.objects.first()
    parts = Parts.objects.all().filter(serial=pk)

    context = {
        'first': first,
        'parts': parts,
        'serial': serial,
    }

    return render(request, 'multserial/serial.html', context)


def PartDetailView(request, pk):
    part = Parts.objects.get(id=pk)
    
    parts = part.serial.parts_set.all()
    serial_name = part.serial.name

    image = MultSerial.objects.get(name=serial_name).image
    country = MultSerial.objects.get(name=serial_name).country
    language = MultSerial.objects.get(name=serial_name).language
    category = MultSerial.objects.get(name=serial_name).category
    date = MultSerial.objects.get(name=serial_name).date
    video = part.part_video
    

    context = {
        'part': part,
        'parts': parts,
        'serial_name': serial_name,
        'image': image,
        'country': country,
        'language': language,
        'category': category,
        'date': date,
        'video': video,
    }

    return render(request, 'multserial/part.html', context)
