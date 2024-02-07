from abc import ABC


class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value


class Branch:
    def __init__(self, source, destination, value=None):
        self.source = source
        self.destination = destination
        self.value = value


class Graph(ABC):
    def __init__(self):
        self.n = {}
        self.b = []

    @property
    def nodes(self):
        return self.n

    @property
    def branches(self):
        return self.b

    def add_node(self, node: Node):
        self.n[node.id] = node

    def add_edge(self, source: Node, destination: Node, value=None):
        if source.id not in self.nodes:
            self.add_node(source)
        if destination.id not in self.nodes:
            self.add_node(destination)

        self.branches.append(Branch(source, destination, value))

    def __str__(self):
        return "".join([f"{b.source.id} ---> {b.destination.id}: {b.value}\n" for b in self.branches])
