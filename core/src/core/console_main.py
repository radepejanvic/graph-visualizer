from typing import List, Union

import pkg_resources

from api.src.api.services.base import DataSourceBase, VisualizerBase
from api.src.api.models.model import Graph,Node


def console_menu(*args, **kwargs):
    plugins: List[Union[DataSourceBase, VisualizerBase]] = \
        kwargs.get("data_sources", []) + kwargs.get("visualizers", [])
    if not plugins:
        print("No plugins found!")
        return

    greska = False
    poruka = None
    while True:
        print("-----------------------------------")
        if greska:
            print("Uneli ste pogresnu vrednost za opciju")
            greska = False
        if poruka:
            print(poruka)
        print("Izaberite broj opcije:")

        for i, plugin in enumerate(plugins):
            print(f"{i} {plugin.identifier()} - {plugin.name()}")
        print("X - exit")
        try:
            izbor = input("Unesite redni broj opcije")
        except:
            greska = True
            continue
        if izbor.upper() == "X":
            return
        elif 0 <= int(izbor) < len(plugins):
            poruka = choosen_option(plugins[int(izbor)], **kwargs)
        else:
            greska = True

def choosen_option(plugin: Union[DataSourceBase, VisualizerBase], **kwargs):
    try:
        if isinstance(plugin, DataSourceBase):
            graph = kwargs["graph"]
            graph = plugin.load()
            return graph
        elif isinstance(plugin, VisualizerBase):
            graph = kwargs["graph"]
            return plugin.display(graph)
    except Exception as e: 
        print(f"Error: {e}")


def load_plugins(group: str):
    plugins = []

    for ep in pkg_resources.iter_entry_points(group=group):
        p = ep.load()
        print(f"{ep.name} {p}")
        plugin = p()
        plugins.append(plugin)

    return plugins


def main():
    try:
        data_sources = load_plugins("data_sources")
        visualizers = load_plugins("visualizers")
    except Exception as e:
        print(f"Error: {e}")
        return

    try:
        graph = Graph()
        console_menu(data_sources=data_sources,
                     visualizers=visualizers,
                     graph=graph)

    except Exception as e:
        print(f"Error: {e}")
        return
