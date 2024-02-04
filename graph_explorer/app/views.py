from django.shortcuts import render
from django.apps.registry import apps

def index(request):
    core = apps.get_app_config("app").core
    return render(request,"index.html", {"title": "Index", "plugini_ucitavanje": core.data_sources})


def nba(request):
    core = apps.get_app_config("app").core
    core.load_graph(0)
    return render(request,"index.html", {"title": "Index", "plugini_ucitavanje": core.data_sources, "main_view": core.display_graph(0)})
