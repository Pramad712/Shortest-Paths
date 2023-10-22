from math import ceil, sqrt
from collections import deque
from priority_queue import PriorityQueue
from constants import GRAPH_LENGTH, GRAPH_HEIGHT, DIAGONAL_DISTANCE, DIAGONAL_DISTANCE_REPR
from graph import Node, NodePathData, draw_node

def solve(window, graph: list[list[Node]], start_node: Node, end_node: Node):
    def distance(path: list[Node], intercardinal_count) -> str:
        result = 0

        for node, next_node in zip(path[: -1], path[1: ]):
            increment = sqrt(abs(next_node.x - node.x) ** 2 + abs(next_node.y - node.y) ** 2)

            if increment % 1 == 0:
                increment = int(increment)

            result += increment

        return f"{len(path) - 1 - intercardinal_count} + {intercardinal_count}{DIAGONAL_DISTANCE_REPR} ≈ {result:.3f}"

    def next_nodes(previous_node: Node, node: Node) -> list[Node]:
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
            if 0 <= node.y + previous_y_change <= GRAPH_HEIGHT and 0 <= node.x + previous_x_change <= GRAPH_LENGTH and graph[node.y + previous_y_change][node.x + previous_x_change].type != "wall":
                nodes.append((graph[node.y + previous_y_change][node.x + previous_x_change], 1 if abs(previous_x_change + previous_y_change) == 1 else DIAGONAL_DISTANCE))

        except IndexError:
            pass

        if abs(previous_x_change + previous_y_change) == 1:
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

    def heuristic(node: Node) -> int:
        # Octile Distance with tie-breaker of 1 + 1/{graph size/2} (super small to avoid over-estimating)
        x_distance, y_distance = abs(end_node.x - node.x), abs(end_node.y - node.y)
        return (x_distance + y_distance + (DIAGONAL_DISTANCE - 2) * min(x_distance, y_distance)) * (1 + 1/ceil((GRAPH_LENGTH * GRAPH_HEIGHT)/2))

    priority_queue = PriorityQueue()
    visited_nodes = set()

    priority_queue.add(NodePathData(start_node, None, 0, float("inf")))

    try:
        while (current_node := priority_queue.pop()).node != end_node:
            if current_node.node != start_node:
                draw_node(window, current_node.node)

            visited_nodes.add(current_node.node)

            for adjacent_node, edge_distance in next_nodes(None if current_node.from_ is None else current_node.from_.node, current_node.node):
                if adjacent_node not in visited_nodes:
                    priority_queue.add(NodePathData(adjacent_node, current_node, current_node.distance_traveled + edge_distance,
                                       current_node.distance_traveled + edge_distance + heuristic(adjacent_node),
                                       current_node.intercardinal_count + (edge_distance == DIAGONAL_DISTANCE)))

    except KeyError:
        return "INVALID", float("inf")

    path = deque([current_node.node])
    node = current_node

    while node.from_ is not None:
        path.appendleft(node.from_.node)
        node = node.from_

    path = list(path)

    return path, distance(path, current_node.intercardinal_count)
