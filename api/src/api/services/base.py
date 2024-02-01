from abc import ABC, abstractmethod

class ServiceBase(ABC):
    @abstractmethod
    def identifier(self):
        pass

    @abstractmethod
    def name(self):
        pass

class DataSourceBase(ServiceBase):

    @abstractmethod
    def load(self):
        pass

class VisualizerBase(ServiceBase): 
    
    @abstractmethod
    def display(self):
        pass