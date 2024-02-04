from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('main/<int:visualizer>/<int:data_source>', views.main_view, name="main_view"),
]
