from django.urls import path
from .views import allseries, SerialDetailView, PartDetailView, CategoryView

urlpatterns = [
    path('', allseries, name='mult-series'),
    path('category/<str:category_name>', CategoryView.as_view(), name='mult-serial-category'),
    path('<int:pk>/mult', SerialDetailView, name='mult-part-serial'),
    path('part/<int:pk>', PartDetailView, name='mult-part-detail'),
]