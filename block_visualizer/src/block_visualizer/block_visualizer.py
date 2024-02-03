from jinja2 import Environment, FileSystemLoader
from api.src.api.services.base import VisualizerBase
from api.src.api.models.model import *

class BlockVisualizer(VisualizerBase):

    def identifier(self) -> str:
        return "BlockVisualizer"

    def name(self) -> str:
        return "BlockVisualizer"

    def display(self,graph:Graph):
        template_dir = "../block_visualizer/src/block_visualizer"
        env = Environment(loader=FileSystemLoader(template_dir))
        template = env.get_template("block.html")
        data = {
            "graph": graph
        }
        return template.render(data)
        
