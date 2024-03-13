from django.urls import path
from .views import allseries, SerialDetailView, PartDetailView, CategoryView

urlpatterns = [
    path('', allseries, name='series'),
    path('category/<str:category_name>', CategoryView.as_view(), name='serial-category'),
    path('<int:pk>/serial', SerialDetailView, name='part-serial'),
    path('part/<int:pk>', PartDetailView, name='part-detail'),
]