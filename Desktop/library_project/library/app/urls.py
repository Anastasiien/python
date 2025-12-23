from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

urlpatterns = [
    path('collection/', views.collection_list, name='collection_list'),
    path('collection/add/', views.collection_create, name='collection_create'),
    path('collection/<int:pk>/edit/', views.collection_update, name='collection_update'),
    path('collection/<int:pk>/delete/', views.collection_delete, name='collection_delete'),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('profile/', views.profile, name='profile'),
]