from django.urls import path

from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('role/create', views.RoleCreateView.as_view(), name='role-create'),
    path('<int:user_id>/assign-role', views.RoleAssignView.as_view(), name='role-assign'),
    path('', views.UserList.as_view(), name='user-list'),
]