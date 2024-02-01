from datetime import datetime

class Node:
    def __init__(self, id,value):
        self.id = id
        self.value = value
        self.branches = []

    def add_branch(self, destination, value=None):
        new_branch = Branch(destination, value)
        self.branches.append(new_branch)

class Branch:
    def __init__(self, destination, value=None):
        self.destination = destination
        self.value = value

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, value:Node):
        self.nodes.append(value)
        return value

    def add_edge(self, source:Node, destination:Node, value=None):
        if source.id not in [node.id for node in self.nodes]:
            self.add_node(source)
        if destination.id not in [node.id for node in self.nodes]:
            self.add_node(destination)

        source_node = next(node for node in self.nodes if node.id == source.id)
        source_node.add_branch(destination, value)

    def printGraph(self):
        for node in self.nodes:
            print(f"Node {node.id}, value:{node.value} :")
            for branch in node.branches:
                print(f"  -> {branch.destination.id}")