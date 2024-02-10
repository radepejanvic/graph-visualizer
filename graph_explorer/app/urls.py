from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('main/<int:visualizer>/<int:data_source>', views.main_view, name="main_view"),
    path('tree/<str:node>', views.get_children, name="get_children"),
    path('workspace/add', views.add_workspace, name='add_workspace'),
    path('workspace/get', views.get_workspace_count, name='get_workspace_count'),
    path('workspace/<int:workspace>', views.switch_workspace, name='switch_workspace'),
    path('filter', views.filter, name='filter')
]
