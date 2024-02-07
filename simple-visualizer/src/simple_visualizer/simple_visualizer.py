from jinja2 import Environment, FileSystemLoader
from api.src.api.services.base import VisualizerBase
from api.src.api.models.model import *


class SimpleVisualizer(VisualizerBase):

    def identifier(self) -> str:
        return "SimpleVisualizer"

    def name(self) -> str:
        return "Simple Visualizer"

    def display(self, graph: Graph):
        template_dir = "../simple-visualizer/src/simple_visualizer"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("simple.html")
        data = {
            "graph": graph
        }
        return template.render(data)

