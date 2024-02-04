from django.shortcuts import render
from django.apps.registry import apps


def index(request):
    core = apps.get_app_config("app").core
    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers}
    return render(request, "index.html", data)


def main_view(request, visualizer: int, data_source: int):
    core = apps.get_app_config("app").core
    core.load_graph(data_source)
    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers,
            "main_view": core.display_graph(visualizer)}
    return render(request, "index.html", data)
