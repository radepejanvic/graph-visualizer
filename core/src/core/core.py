from abc import ABC
from typing import List
import pkg_resources

from api.src.api.models.model import Graph
from api.src.api.services.base import DataSourceBase, VisualizerBase

DATA_SOURCES = "data_sources"
VISUALIZERS = "visualizers"


class Core(ABC):

    def __init__(self):
        self.g: Graph = Graph()
        self.ds: List[DataSourceBase] = self._load_plugins(DATA_SOURCES)
        self.vs: List[VisualizerBase] = self._load_plugins(VISUALIZERS)

    @property
    def graph(self) -> Graph:
        return self.g

    @graph.setter
    def graph(self, new_graph):
        self.g = new_graph

    @property
    def data_sources(self) -> List[DataSourceBase]:
        return self.ds

    @property
    def visualizers(self) -> List[VisualizerBase]:
        return self.vs

    def _load_plugins(self, group: str) -> list:
        plugins = []

        for ep in pkg_resources.iter_entry_points(group=group):
            p = ep.load()
            print(f"{ep.name} {p}")
            plugin = p()
            plugins.append(plugin)

        return plugins

    def load_graph(self, data_source: int):
        self.g = self.ds[data_source].load()

    def display_graph(self, visualizer: int) -> str:
        return self.vs[visualizer].display(self.g)
