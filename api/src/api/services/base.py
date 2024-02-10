from abc import ABC, abstractmethod
from ..models.model import *


class ServiceBase(ABC):
    @abstractmethod
    def identifier(self) -> str:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


class DataSourceBase(ServiceBase):

    @abstractmethod
    def load(self) -> Graph:
        pass


class VisualizerBase(ServiceBase):

    @abstractmethod
    def display(self, graph: Graph) -> str:
        pass
