from abc import ABC


class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value


class Branch:
    def __init__(self, source, destination, value=None, directed=False):
        self.source = source
        self.destination = destination
        self.value = value
        self.directed = directed

    def __contains__(self, item):
        return self.source == item or self.destination == item

    def __str__(self):
        return f"{self.source} {"-->" if self.directed else "---"} {self.destination}: {self.value}"


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

    def add_branch(self, source: Node, destination: Node, value=None):
        if source.id not in self.nodes:
            self.add_node(source)
        if destination.id not in self.nodes:
            self.add_node(destination)

        self.branches.append(Branch(source.id, destination.id, value))

    def get_branches_for_node(self, node):
        return [branch for branch in self.b if node in branch]

    def __str__(self):
        return "".join([f"{str(branch)}\n" for branch in self.b])
