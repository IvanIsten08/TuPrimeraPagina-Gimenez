from django.urls import path

from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('categorias/list/', views.categoria_list, name='categoria_list'),
    path('categorias/create/', views.categoria_create, name='categoria_create'),
]