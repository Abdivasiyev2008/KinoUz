from typing import Any, Dict
from django.shortcuts import render, redirect
from .models import Cartoon, Category, CartoonComment
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def all_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}

def allCartoons(request):
    cartoons = Cartoon.objects.all()
    random_cartoon = np.random.choice(cartoons, size=1, replace=False)
    random_cartoons = np.random.choice(cartoons, size=3, replace=False)
    categories = Category.objects.all()

    q=request.GET.get('q', '')
    if q:
        cartoons = cartoons.filter(name__icontains=q)
    
    return render(request, 'cartoons/list.html', {'categories': categories, 'cartoons': cartoons, 'random_cartoons': random_cartoons, 'random_cartoon': random_cartoon, })

class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)
        cartoons = Cartoon.objects.filter(category=category)

        q=request.GET.get('q', '')

        if q:
            cartoons = cartoons.filter(name__icontains=q)

        return render(request, "cartoons/category.html", {'cartoons': cartoons, "category":category, })

class CartoonDetailView(DetailView):
    model = Cartoon
    template_name = 'cartoons/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_cartoons = Cartoon.objects.all()
        random_cartoons = np.random.choice(all_cartoons, size=4, replace=False)
        context["random_cartoons"] = random_cartoons
        
        return context
    
@login_required(login_url='login')
def new_comment(request, cartoon_id):
    cartoon = get_object_or_404(Cartoon, id=cartoon_id)   
    if request.method == 'POST':
        CartoonComment.objects.create(
            user = request.user,
            cartoon= cartoon,
            body = request.POST['body']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('cartoon-detail', cartoon_id)
    return HttpResponse("add comment")

@login_required(login_url='login')
def delete_comment(request, cartoon_id, comment_id):
    comment = get_object_or_404(CartoonComment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
        return redirect('cartoon-detail', cartoon_id)
    return redirect('cartoon-detail', cartoon_id)