from api.src.api.models.model import Graph

def check_condition(value, operator, value_filter):
    if operator == ">":
        return value > value_filter
    elif operator == "<":
        return value < value_filter
    elif operator == "=":
        return value == value_filter
    elif operator == "!=":
        return value != value_filter
    else:
        return False


def filter(graph:Graph, key:str,value_filter:str|int|float,operation:str):
    
    if isinstance(value_filter, (int, float)):
        new_nodes = {node.id: node for node in graph.n.values() if check_condition(node.value[key], operation, value_filter)}
    else:
        new_nodes = {node.id: node for node in graph.n.values() if check_condition(str(node.value[key]), operation, value_filter)}

    graph.n = new_nodes
    
    new_branches = [branch for branch in graph.b if branch.source in graph.n and branch.destination in graph.n]
    graph.b = new_branches
    

def search(graph:Graph, query: str | int | float):
    
    if isinstance(query, (int, float)):
        new_nodes = {node.id: node for node in graph.n.values() if query in node.value.values() or query in node.id}
    else:
        new_nodes = {node.id: node for node in graph.n.values() if any(value is not None and query in value for value in node.value.values()) or query in node.id}

    graph.n = new_nodes
    new_branches = [branch for branch in graph.b if branch.source in graph.n and branch.destination in graph.n]
    graph.b = new_branches
