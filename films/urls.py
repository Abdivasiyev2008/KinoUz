from django.urls import path
from .views import allFilms, CategoryView, FilmDetailView, new_comment, delete_comment

urlpatterns = [
    path('', allFilms, name='home'),
    path('films/<str:category_name>/', CategoryView.as_view(), name='film-category'),
    path('<int:pk>/film', FilmDetailView.as_view(), name='film-detail'),
    path("<int:film_id>/comment/new", new_comment, name='comment_new'),
    path("<int:film_id>/comment/<int:comment_id>/delete", delete_comment, name='comment_delete'),
]