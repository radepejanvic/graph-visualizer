from django.http import JsonResponse
from django.shortcuts import render
from django.apps.registry import apps
from django.core.serializers.json import DjangoJSONEncoder
import json
import re

from django import forms

class MyForm(forms.Form):
    filter = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Search & filter'}))

def index(request):
    core = apps.get_app_config("app").core
    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers}
    return render(request, "index.html", data)


def main_view(request, visualizer: int, data_source: int):
    core = apps.get_app_config("app").core
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            filter = form.cleaned_data['filter']
            operators = {'>': '>', '<': '<', '=': '=', '!=': '!='}
            pattern = re.compile(r'[<>!=]')

            match = pattern.search(filter)
            if match:
                operator, value = re.split(r'\s*{}\s*'.format(match.group()), filter)
                try:
                    value = int(value)  
                except ValueError:
                    pass
                
                core.filter_graph(operator, value, operators[match.group()])
                

            else:
                core.search_graph(filter)
    else:
        form = MyForm()
        core.load_graph(data_source)
          
    data = {"title": "Index",
            "data_sources": core.data_sources,
            "visualizers": core.visualizers,
            "main_view": core.display_graph(visualizer),
            "nodes": core.graph.nodes.keys(),
            "forma":form}
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
