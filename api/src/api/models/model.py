from datetime import datetime

class Node:
    def __init__(self, id,value):
        self.id = id
        self.value = value

class Branch:
    def __init__(self,source, destination, value=None):
        self.source = source
        self.destination = destination
        self.value = value

class Graph:
    def __init__(self):
        self.nodes = []
        self.branches = []

    def add_node(self, value:Node):
        self.nodes.append(value)
        return value

    def add_edge(self, source:Node, destination:Node, value=None):
        if source.id not in [node.id for node in self.nodes]:
            self.add_node(source)
        if destination.id not in [node.id for node in self.nodes]:
            self.add_node(destination)

        source_node = next(node for node in self.nodes if node.id == source.id)
        destination_node = next(node for node in self.nodes if node.id == destination.id)
        self.branches.append(Branch(source_node,destination_node,value))

    def printGraph(self):
        for br in self.branches:
            print(f"Branch {br.source.id} ---> {br.destination.id} :{br.value}")
