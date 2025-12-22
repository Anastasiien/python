from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('collection/', views.collection_list, name='collection_list'),
    path('collection/add/', views.collection_create, name='collection_create'),
    path('collection/<int:pk>/edit/', views.collection_update, name='collection_update'),
    path('collection/<int:pk>/delete/', views.collection_delete, name='collection_delete'),
]