from sys import setrecursionlimit
from types import FunctionType
from graph import Node

def solve(adjacent: FunctionType, graph: list[list[Node]], start_node: Node, end_node: Node):
    setrecursionlimit(2 ** 31 - 1)

    minimum_path_per_node = {node: float("inf") for row in graph for node in row}
    minimum_path_per_node[start_node] = float("nan")

    best_path = []

    def heuristic(node: Node):
        return abs(end_node.x - node.x) ** 2 + abs(end_node.y - node.y) ** 2

    def a_star(node: Node, path: set[Node], path_list: list[Node], weight: int = 0):
        nonlocal minimum_path_per_node

        if node == end_node:
            minimum_path_per_node[node] = weight

            nonlocal best_path
            best_path = path_list.copy()

            return "FOUND"

        if weight != 0:
            path = path.copy()
            path.add(node)

            path_list = path_list.copy()
            path_list.append(node)

            minimum_path_per_node[node] = weight

        heuristic_blocks = {}

        for adjacent_node, edge_weight in adjacent(node, graph):
            if adjacent_node in path:
                continue

            current_heuristic = heuristic(adjacent_node)

            try:
                heuristic_blocks[current_heuristic].append((adjacent_node, edge_weight))

            except KeyError:
                heuristic_blocks[current_heuristic] = [(adjacent_node, edge_weight)]

        heuristic_blocks = sorted(heuristic_blocks.items())

        for _, nodes in heuristic_blocks:
            for adjacent_node, edge_weight in nodes:
                found = False

                if weight + edge_weight < minimum_path_per_node[adjacent_node]:
                    found = max(found, bool(a_star(adjacent_node, path, path_list, weight + edge_weight)))

                if found:
                    return "FOUND"

    found = a_star(start_node, set(), [])

    if found:
        return best_path, minimum_path_per_node[end_node]

    else:
        return "INVALID"
