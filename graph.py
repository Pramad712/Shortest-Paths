import pygame
from types import SimpleNamespace
from constants import *

class Node(SimpleNamespace):
    x: int
    y: int
    type: str

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __hash__(self):
        return hash((self.x, self.y, self.type))

def create_graph():
    return [[Node(x=x, y=y, type="cell") for x in range(GRAPH_LENGTH)] for y in range(GRAPH_HEIGHT)]

def adjacent(node: Node, graph: list[list[Node]]):
    adjacent_nodes = []

    if node.y > 0 and graph[node.y - 1][node.x].type != "wall":
        adjacent_nodes.append((graph[node.y - 1][node.x], 1))

    if node.x < GRAPH_LENGTH - 1 and node.y > 0 and graph[node.y - 1][node.x + 1].type != "wall":
        adjacent_nodes.append((graph[node.y - 1][node.x + 1], DIAGONAL_LENGTH))

    if node.x < GRAPH_LENGTH - 1 and graph[node.y][node.x + 1].type != "wall":
        adjacent_nodes.append((graph[node.y][node.x + 1], 1))

    if node.x < GRAPH_LENGTH - 1 and node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x + 1].type != "wall":
        adjacent_nodes.append((graph[node.y + 1][node.x + 1], DIAGONAL_LENGTH))

    if node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x].type != "wall":
        adjacent_nodes.append((graph[node.y + 1][node.x], 1))

    if node.x > 0 and node.y < GRAPH_HEIGHT - 1 and graph[node.y + 1][node.x - 1].type != "wall":
        adjacent_nodes.append((graph[node.y + 1][node.x - 1], DIAGONAL_LENGTH))

    if node.x > 0 and graph[node.y][node.x - 1].type != "wall":
        adjacent_nodes.append((graph[node.y][node.x - 1], 1))

    if node.x > 0 and node.y > 0 and graph[node.y - 1][node.x - 1].type != "wall":
        adjacent_nodes.append((graph[node.y - 1][node.x - 1], DIAGONAL_LENGTH))

    return adjacent_nodes

def draw_graph(window: pygame.Surface, graph: list[list[Node]]):
    for row_index, row in enumerate(graph):
        y = TOP_OFFSET + row_index * NODE_HEIGHT

        for x, node in enumerate(row):
            x = LEFT_OFFSET + x * NODE_LENGTH

            color = None

            match node.type:
                case "cell":
                    color = CELL_COLOR

                case "wall":
                    color = WALL_COLOR

                case "start":
                    color = START_COLOR

                case "end":
                    color = END_COLOR

                case "path":
                    color = PATH_COLOR

            pygame.draw.rect(window, color, pygame.Rect((x, y), (NODE_LENGTH, NODE_HEIGHT)))

    for y_coordinate in range(TOP_OFFSET, HEIGHT - BOTTOM_OFFSET + 1, NODE_HEIGHT):
        pygame.draw.line(window, BORDER_COLOR, (LEFT_OFFSET, y_coordinate), (LENGTH - RIGHT_OFFSET, y_coordinate))

    for x_coordinate in range(LEFT_OFFSET, LENGTH - RIGHT_OFFSET + 1, NODE_LENGTH):
        pygame.draw.line(window, BORDER_COLOR, (x_coordinate, TOP_OFFSET), (x_coordinate, HEIGHT - BOTTOM_OFFSET))

    pygame.display.update()

def write_instruction(window: pygame.Surface, text: str, icon_string: str = None):
    clear_message(window)

    icon_size = 20 if icon_string is not None else 0

    text = FONT.render(text, 1, TEXT_COLOR)
    window.blit(text, (LENGTH / 2 - (text.get_width() + icon_size * 2) / 2, (TOP_OFFSET - text.get_height()) / 2))

    if icon_size == 0:
        pygame.display.update()
        return

    icon = pygame.Rect(
        (LENGTH / 2 + (text.get_width() + icon_size * 2) / 2 - icon_size, TOP_OFFSET // 2 - icon_size // 2),
        (icon_size, icon_size))

    color = None

    match icon_string:
        case "start":
            color = START_COLOR

        case "end":
            color = END_COLOR

        case "wall":
            color = WALL_COLOR

    pygame.draw.rect(window, color, icon)

    pygame.display.update()

def clear_message(window: pygame.Surface):
    pygame.draw.rect(window, EMPTY_COLOR, pygame.Rect((0, 0), (LENGTH, TOP_OFFSET)))
    pygame.display.update()

def draw_button(window: pygame.Surface, text: str):
    button = pygame.Rect(((LENGTH - BUTTON_LENGTH) // 2, HEIGHT - BOTTOM_OFFSET // 2 - BUTTON_HEIGHT // 2), (BUTTON_LENGTH, BUTTON_HEIGHT))
    pygame.draw.rect(window, BUTTON_COLOR, button)

    text = FONT.render(text, 1, TEXT_COLOR)
    window.blit(text, ((LENGTH - text.get_width()) // 2, HEIGHT - (BOTTOM_OFFSET + text.get_height()) // 2))

    pygame.display.update()

    return button

def clear_button(window: pygame.Surface):
    pygame.draw.rect(window, EMPTY_COLOR, pygame.Rect((0, HEIGHT - BOTTOM_OFFSET + 1), (LENGTH, BOTTOM_OFFSET - 1))) # The 1 excludes the line on the bottom of the graph.
    pygame.display.update()

def draw_path(window: pygame.Surface, path: tuple[list[Node], int], graph: list[list[Node]]):
    for node in path[0]:
        graph[node.y][node.x].type = "path"

    draw_graph(window, graph)
