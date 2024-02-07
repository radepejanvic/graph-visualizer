class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value


class Branch:
    def __init__(self, source, destination, value=None):
        self.source = source
        self.destination = destination
        self.value = value


class Graph:
    def __init__(self):
        self.nodes = {}
        self.branches = []

    def add_node(self, node: Node):
        self.nodes[node.id] = node

    def add_edge(self, source: Node, destination: Node, value=None):
        if source.id not in self.nodes:
            self.add_node(source)
        if destination.id not in self.nodes:
            self.add_node(destination)

        self.branches.append(Branch(source, destination, value))

    def __str__(self):
        # return "".join([f"{node.id} ---> {node.value}\n" for node in self.nodes.values()])
        return "".join([f"{b.source.id} ---> {b.destination.id}: {b.value}\n" for b in self.branches])
