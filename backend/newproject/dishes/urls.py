from django.urls import path
from . import views

urlpatterns = [
    path('', views.MenuApiView.dishes_create, name='dishes-create'),
    path('list/', views.MenuApiView.dishes_list, name='dishes-list'),
]

