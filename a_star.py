from sys import setrecursionlimit
from math import ceil
from constants import GRAPH_LENGTH, GRAPH_HEIGHT, DIAGONAL_DISTANCE
from graph import Node, draw_node

def solve(window, graph: list[list[Node]], start_node: Node, end_node: Node):
    def next_nodes(previous_node: Node, node: Node):
        # Uses JPS (Jump Point Search), but no jumping because this is just for adjacency,
        if previous_node is None:
            nodes = []

            if node.y > 0 and graph[node.y - 1][node.x].type != "wall":
                nodes.append((graph[node.y - 1][node.x], 1))

            if node.x < GRAPH_LENGTH - 1 and node.y > 0 and graph[node.y - 1][node.x + 1].type != "wall":
                nodes.append((graph[node.y - 1][node.x + 1], DIAGONAL_DISTANCE))

            if node.x < GRAPH_LENGTH - 1 and graph[node.y][node.x + 1].type != "wall":
                nodes.append((graph[node.y][node.x + 1], 1))

            if node.x < GRAPH_LENGTH - 1 and node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x + 1].type != "wall":
                nodes.append((graph[node.y + 1][node.x + 1], DIAGONAL_DISTANCE))

            if node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x].type != "wall":
                nodes.append((graph[node.y + 1][node.x], 1))

            if node.x > 0 and node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x - 1].type != "wall":
                nodes.append((graph[node.y + 1][node.x - 1], DIAGONAL_DISTANCE))

            if node.x > 0 and graph[node.y][node.x - 1].type != "wall":
                nodes.append((graph[node.y][node.x - 1], 1))

            if node.x > 0 and node.y > 0 and graph[node.y - 1][node.x - 1].type != "wall":
                nodes.append((graph[node.y - 1][node.x - 1], DIAGONAL_DISTANCE))

            return nodes

        previous_x_change, previous_y_change = node.x - previous_node.x, node.y - previous_node.y

        nodes = []

        try:
            if 0 <= node.y + previous_y_change and 0 <= node.x + previous_x_change and graph[node.y + previous_y_change][node.x + previous_x_change].type != "wall":
                nodes.append((graph[node.y + previous_y_change][node.x + previous_x_change], 1))

        except IndexError:
            pass

        if abs(previous_x_change) + abs(previous_y_change) == 1:
            if abs(previous_x_change) + abs(previous_y_change) == 1:
                if previous_x_change != 0:
                    change = previous_x_change

                    if 0 <= node.y - change <= GRAPH_HEIGHT - 1 and 0 <= node.x + change <= GRAPH_LENGTH - 1 and graph[node.y - change][node.x + change].type != "wall":
                        nodes.append((graph[node.y - change][node.x + change], DIAGONAL_DISTANCE))

                    if 0 <= node.y + change <= GRAPH_HEIGHT - 1 and 0 <= node.x + change <= GRAPH_LENGTH - 1 and graph[node.y + change][node.x + change].type != "wall":
                        nodes.append((graph[node.y + change][node.x + change], DIAGONAL_DISTANCE))

                else:
                    change = previous_y_change

                    if 0 <= node.y + change <= GRAPH_HEIGHT - 1 and 0 <= node.x - change <= GRAPH_LENGTH - 1 and graph[node.y + change][node.x - change].type != "wall":
                        nodes.append((graph[node.y + change][node.x - change], DIAGONAL_DISTANCE))

                    if 0 <= node.y + change <= GRAPH_HEIGHT - 1 and 0 <= node.x + change <= GRAPH_LENGTH - 1 and graph[node.y + change][node.x + change].type != "wall":
                        nodes.append((graph[node.y + change][node.x + change], DIAGONAL_DISTANCE))

        else:
            if 0 <= node.x + previous_x_change <= GRAPH_LENGTH - 1 and graph[node.y][node.x + previous_x_change].type != "wall":
                nodes.append((graph[node.y][node.x + previous_x_change], 1))

            if 0 <= node.y + previous_y_change <= GRAPH_HEIGHT - 1 and graph[node.y + previous_y_change][node.x].type != "wall":
                nodes.append((graph[node.y + previous_y_change][node.x], 1))

            if 0 <= node.y + previous_y_change <= GRAPH_HEIGHT - 1 and graph[node.y][previous_node.x].type == "wall" and graph[node.y + previous_y_change][previous_node.x].type != "wall":
                nodes.append((graph[node.y + previous_y_change][previous_node.x], DIAGONAL_DISTANCE))

            if 0 <= node.x + previous_x_change <= GRAPH_HEIGHT - 1 and graph[previous_node.y][node.x].type == "wall" and graph[previous_node.y][node.x + previous_x_change].type != "wall":
                nodes.append((graph[previous_node.y][node.x + previous_x_change], DIAGONAL_DISTANCE))

        return nodes

    setrecursionlimit(2 ** 31 - 1)

    minimum_path_per_node = {node: float("inf") for row in graph for node in row}
    minimum_path_per_node[start_node] = float("nan")

    visited = set()
    best_path = []

    def heuristic(node: Node):
        # Octile Distance with tie-breaker of 1 + 1/{graph size/2} (super small to avoid over-estimating)
        x_distance, y_distance = abs(end_node.x - node.x), abs(end_node.y - node.y)
        return (x_distance + y_distance + (DIAGONAL_DISTANCE - 2) * min(x_distance, y_distance)) * (1 + 1/ceil((GRAPH_LENGTH * GRAPH_HEIGHT)/2))

    def a_star(previous_node: Node, node: Node, path: set[Node], path_list: list[Node], weight: int = None):
        nonlocal minimum_path_per_node
        nonlocal visited

        visited.add(node)

        path = path.copy()
        path.add(node)

        path_list = path_list.copy()
        path_list.append(node)

        if weight is not None:
            minimum_path_per_node[node] = min(minimum_path_per_node[node], weight)

        if node == end_node:
            nonlocal best_path
            best_path = path_list.copy()

            return True

        # Comment out the following two lines if you don't want to see the explored nodes that aren't in the path.
        if weight is not None:
            draw_node(window, node)

        if weight is None:
            weight = 0

        distances = []

        for adjacent_node, edge_weight in next_nodes(previous_node, node):
            if (adjacent_node in visited) or (weight + edge_weight >= minimum_path_per_node.get(adjacent_node)):
                continue

            current_heuristic = heuristic(adjacent_node)
            distances.append((edge_weight, current_heuristic, adjacent_node))

        distances.sort(key=lambda distance: distance[0] + distance[1])

        for edge_weight, _, adjacent_node in distances:
            if adjacent_node in visited:
                continue

            found = a_star(node, adjacent_node, path, path_list, weight + edge_weight)

            if found:
                return True

    found = a_star(None, start_node, set(), [])

    if found:
        return best_path, minimum_path_per_node[end_node]

    else:
        return "INVALID"
