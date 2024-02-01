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
