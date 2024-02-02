from typing import List, Union

import pkg_resources

from api.src.api.services.base import DataSourceBase, VisualizerBase


def console_menu(*args, **kwargs):
    plugins: List[Union[DataSourceBase, VisualizerBase]] = \
        kwargs.get("data_sources", []) + kwargs.get("visualizers", [])
    if not plugins:
        print("No plugins found!")
        return

    for i, plugin in enumerate(plugins):
        print(f"{i} {plugin.identifier()} - {plugin.name()}")
    print("X - exit")


# def izabrana_opcija(plugin: Union[DataSourceBase, VisualizerBase], **kwargs):
#     try:
#         if isinstance(plugin, DataSourceBase):
#             fakulteti = kwargs["fakulteti"]
#             pomocna_lista = plugin.ucitati_fakultete()
#             del fakulteti[:]
#             fakulteti.extend(pomocna_lista)
#             return "Ucitani fakulteti"
#         elif isinstance(plugin, FakultetPrikazBase):
#             fakulteti = kwargs["fakulteti"]
#             return plugin.prikazati_fakultete(fakulteti)
#     except Exception as e:
#         print(f"Error: {e}")


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
        console_menu(data_sources=data_sources,
                     visualizers=visualizers)

    except Exception as e:
        print(f"Error: {e}")
        return
