from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('about/', views.about, name='about'),

]
