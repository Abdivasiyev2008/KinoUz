from django.shortcuts import render, redirect
from .models import Film, Comment, Category
from django.shortcuts import get_object_or_404
from django.views import View
from django.views.generic import DetailView
import numpy as np
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.

def allFilms(request):
    films = Film.objects.all()
    categories = Category.objects.all()
    
    try:
        random_film = np.random.choice(films, size=1, replace=False)
        random_films = np.random.choice(films, size=3, replace=False)

    except:
        pass

    q=request.GET.get('q', '')
    if q:
        films = films.filter(name__icontains=q)
    
    return render(request, 'films/list.html', {'categories':categories, 'films': films, 'random_films': random_films, 'random_film': random_film, })

class CategoryView(View):
    def get(self, request, category_name):
        category = get_object_or_404(Category, name=category_name)

        films = Film.objects.filter(category=category)

        q=request.GET.get('q', '')

        if q:
            films = films.filter(name__icontains=q)

        return render(request, "films/category.html", {'films':films, "category":category, })

class FilmDetailView(DetailView):
    model = Film
    template_name = 'films/detail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_films = Film.objects.all()
        random_films = np.random.choice(all_films, size=4, replace=False)
        context["random_films"] = random_films
        
        return context
    
@login_required(login_url='login')
def new_comment(request, film_id):
    film = get_object_or_404(Film, id=film_id)   
    if request.method == 'POST':
        Comment.objects.create(
            user = request.user,
            film= film,
            body = request.POST['body']
        )
        messages.info(request, 'Successfully Sended!')
        return redirect('film-detail', film_id)
    return HttpResponse("add comment")

@login_required(login_url='login')
def delete_comment(request, film_id, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
        messages.info(request, 'Successfully Deleted!')
    
        return redirect('film-detail', film_id)
    
    return redirect('film-detail', film_id)

def error_404(request, exception):
    return render(request, 'errors/404.html')