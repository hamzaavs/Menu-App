from django.urls import path
from dishes.views import DishesList, DishesCreate, Dish

urlpatterns = [
    path('', DishesCreate.as_view()),
    path('list/', DishesList.as_view()),
    path('<int:pk>/', Dish.as_view()),
]

