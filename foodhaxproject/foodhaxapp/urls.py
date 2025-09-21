from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic_view, name='basic'),
    path('bread/', views.bread_view, name='bread'),
    path('jubileepantry/', views.jubileepantry_views, name='jubileepantry'),
    path('jubileekitch/', views.jubileekitch_views, name='jubileekitch'),
]