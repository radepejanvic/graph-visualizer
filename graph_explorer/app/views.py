from django.http import JsonResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.core.serializers.json import DjangoJSONEncoder
import json


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
            "main_view": core.display_graph(visualizer),
            "nodes": core.graph.nodes.keys()}
    return render(request, "index.html", data)


def get_children(request, node):
    core = apps.get_app_config("app").core
    # TODO: Move this line to another layer
    data = json.dumps([branch.__dict__ for branch in core.graph.get_branches_for_node(node)], cls=DjangoJSONEncoder)

    return JsonResponse(data, safe=False) if request.method == 'GET' else JsonResponse({}, safe=False)

def switch_workspace(request, workspace):

    pass

def add_workspace(request):
    pass
