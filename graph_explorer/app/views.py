from django.shortcuts import render
from django.http import HttpResponse
from core.console_main import *


def index(request):
    return render(request,"index.html", {"title": "Index", "plugini_ucitavanje": load_plugins("data_sources")})


def nba(request):
    graph = load_plugins("data_sources")[0].load()
    graph.printGraph()
    return render(request,"index.html", {"title": "Index", "plugini_ucitavanje": load_plugins("data_sources"),"main_view": load_plugins("visualizers")[0].display(graph)})
