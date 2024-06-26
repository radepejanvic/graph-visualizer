from django.http import JsonResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.core.serializers.json import DjangoJSONEncoder
import json
import re


def index(request):
    core = apps.get_app_config("app").core
    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers}
    return render(request, "index.html", data)


def main_view(request, visualizer: int, data_source: int):
    app = apps.get_app_config("app")
    core = app.core

    app.visualizer = visualizer
    app.data_source = data_source

    core.load_graph(data_source)

    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers,
            "main_view": core.display_graph(visualizer),
            "nodes": core.graph.nodes.keys()}
    return render(request, "index.html", data)


def filter(request):
    app = apps.get_app_config("app")
    core = app.core

    if request.method == 'POST':
        query = request.POST.get("query", False).strip()

        operators = {'>': '>', '<': '<', '=': '=', '!=': '!='}
        pattern = re.compile(r'[<>!=]')

        match = pattern.search(query)

        if match:
            operator, value = re.split(r'\s*{}\s*'.format(match.group()), query)
            try:
                value = int(value)
            except ValueError:
                pass

            core.filter_graph(operator, value, operators[match.group()])
        else:
            core.search_graph(query)

    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers,
            "main_view": core.display_graph(app.visualizer),
            "nodes": core.graph.nodes.keys()}
    return render(request, "index.html", data)


def get_children(request, node):
    core = apps.get_app_config("app").core
    # TODO: Move this line to another layer
    data = json.dumps([branch.__dict__ for branch in core.graph.get_branches_for_node(node)], cls=DjangoJSONEncoder)

    return JsonResponse(data, safe=False) if request.method == 'GET' else JsonResponse({}, safe=False)


def add_workspace(request):
    app = apps.get_app_config("app")
    app.add_workspace()

    data = {"message": f"Workspace count: {len(app.workspaces)}"}
    return JsonResponse(data)


def get_workspace_count(request):
    app = apps.get_app_config("app")

    data = {"count": f"{len(app.workspaces)}"}
    return JsonResponse(data)


def switch_workspace(request, workspace: int):
    app = apps.get_app_config("app")
    app.switch_workspace(workspace)
    core = app.core

    main_view_render = core.display_graph(app.visualizer) if app.visualizer is not None else ""

    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers,
            "main_view": main_view_render,
            "nodes": core.graph.nodes.keys()}

    return render(request, "index.html", data)



