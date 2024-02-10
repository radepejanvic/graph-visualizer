from django.apps import AppConfig
from core.src.core.core import Core
from typing import List, Dict


class AppConfig(AppConfig):
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'app'
    workspace: Dict
    workspaces: List[Dict]

    def ready(self):
        self.workspace = {"core": Core(), "vs": None, "ds": None}
        self.workspaces = [self.workspace]

    def add_workspace(self):
        self.workspaces.append({"core": Core(), "vs": None, "ds": None})

    def switch_workspace(self, workspace):
        self.workspace = self.workspaces[workspace]

    @property
    def core(self):
        return self.workspace["core"]

    @property
    def visualizer(self):
        return self.workspace["vs"]

    @property
    def data_source(self):
        return self.workspace["ds"]

    @visualizer.setter
    def visualizer(self, vs: int):
        self.workspace["vs"] = vs

    @data_source.setter
    def data_source(self, ds: int):
        self.workspace["ds"] = ds
