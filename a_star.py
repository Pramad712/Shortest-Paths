from sys import setrecursionlimit
from types import FunctionType
from graph import Node

def solve(adjacent: FunctionType, graph: list[list[Node]], start_node: Node, end_node: Node):
    setrecursionlimit(2 ** 31 - 1)

    minimum_path_per_node = {node: float("inf") for row in graph for node in row}
    minimum_path_per_node[start_node] = float("nan")
    minimum_path_per_node[end_node] = False

    best_path = []

    def hueristic(node: Node):
        return abs(end_node.x - node.x) ** 2 + abs(end_node.y - node.y) ** 2

    def a_star(node: Node, path: set[Node], path_list: list[Node], weight: int = 0):
        nonlocal minimum_path_per_node

        if node == end_node:
            minimum_path_per_node[node] = weight

            nonlocal best_path
            best_path = path_list.copy()

            return

        if weight != 0:
            path = path.copy()
            path.add(node)

            path_list = path_list.copy()
            path_list.append(node)

            minimum_path_per_node[node] = weight

        best_heuristic = float("inf")
        best_nodes = []

        for adjacent_node, edge_weight in adjacent(node, graph):
            if adjacent_node in path:
                continue

            current_hueristic = hueristic(adjacent_node)

            if current_hueristic < best_heuristic:
                best_heuristic = current_hueristic
                best_nodes = [(adjacent_node, edge_weight)]

            elif current_hueristic == best_heuristic:
                best_nodes.append((adjacent_node, edge_weight))

        for adjacent_node, edge_weight in best_nodes:
            if weight + edge_weight < minimum_path_per_node[adjacent_node] or minimum_path_per_node[adjacent_node] is False:
                a_star(adjacent_node, path, path_list, weight + edge_weight)

    a_star(start_node, set(), [])

    if minimum_path_per_node[end_node] is not False:
        return best_path, minimum_path_per_node[end_node]

    else:
        return "INVALID"
