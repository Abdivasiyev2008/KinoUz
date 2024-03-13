from django.urls import path
from .views import allCartoons, CategoryView, CartoonDetailView, new_comment, delete_comment

urlpatterns = [
    path('', allCartoons, name='cartoons'),
    path('cartoons/<str:category_name>/', CategoryView.as_view(), name='cartoon-category'),
    path('<int:pk>/cartoon', CartoonDetailView.as_view(), name='cartoon-detail'),
    path("<int:cartoon_id>/comment/new", new_comment, name='cartoon_comment_new'),
    path("<int:cartoon_id>/comment/<int:comment_id>/delete", delete_comment, name='cartoon_comment_delete'),
]