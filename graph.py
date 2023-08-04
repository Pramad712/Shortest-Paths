import pygame
from typing import Any
from dataclasses import dataclass, field
from constants import *

@dataclass
class Node:
    x: int
    y: int
    type: str

    def __hash__(self):
        return hash((self.x, self.y, self.type))

@dataclass(order=True)
class NodePathData:
    node: Node = field(compare=False)
    from_: Any = field(compare=False) # Actually it's NodePathData, but Any is used to avoid self-referencing
    distance_traveled: int | float = field(compare=False)
    total_distance: int | float
    intercardinal_count: int = field(compare=False, default=0)

    def __hash__(self):
        return hash((self.node, self.from_, self.distance_traveled, self.total_distance, self.intercardinal_count))

def create_graph():
    return [[Node(x, y, "cell") for x in range(GRAPH_LENGTH)] for y in range(GRAPH_HEIGHT)]

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

            pygame.draw.rect(window, color, pygame.Rect((x, y), (NODE_LENGTH, NODE_HEIGHT)))

    for y_coordinate in range(TOP_OFFSET, HEIGHT - BOTTOM_OFFSET + 1, NODE_HEIGHT):
        pygame.draw.line(window, BORDER_COLOR, (LEFT_OFFSET, y_coordinate), (LENGTH - RIGHT_OFFSET, y_coordinate))

    for x_coordinate in range(LEFT_OFFSET, LENGTH - RIGHT_OFFSET + 1, NODE_LENGTH):
        pygame.draw.line(window, BORDER_COLOR, (x_coordinate, TOP_OFFSET), (x_coordinate, HEIGHT - BOTTOM_OFFSET))

    pygame.display.update()

def write_instruction(window: pygame.Surface, text: str, icon_string: str = None):
    clear_message(window)

    icon_length, icon_height = (NODE_LENGTH, NODE_HEIGHT) if icon_string is not None else (0, 0)

    text = FONT.render(text, 1, TEXT_COLOR)
    window.blit(text, (LENGTH / 2 - (text.get_width() + icon_length * 2) / 2, (TOP_OFFSET - text.get_height()) / 2))

    if icon_length == icon_height == 0:
        pygame.display.update()
        return

    icon = pygame.Rect((LENGTH / 2 + (text.get_width() + icon_length * 2) / 2 - icon_length, TOP_OFFSET // 2 - icon_height // 2), (icon_length, icon_height))

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
    pygame.draw.rect(window, EMPTY_COLOR, pygame.Rect((0, HEIGHT - BOTTOM_OFFSET + 1), (LENGTH, BOTTOM_OFFSET - 1)))  # The 1 excludes the line on the bottom of the graph.
    pygame.display.update()

def draw_node(window: pygame.Surface, node: Node, color: tuple[int] = PROCESSING_NODE_COLOR):
    pygame.draw.rect(window, color, pygame.Rect((LEFT_OFFSET + node.x * NODE_LENGTH, TOP_OFFSET + node.y * NODE_HEIGHT), (NODE_LENGTH, NODE_HEIGHT)))
    pygame.display.update()

def draw_path(window: pygame.Surface, path: list[list[Node], int]):
    for node in path[1: -1]: # We want to ignore the total edge weight and the start and end positions.
        draw_node(window, node, PATH_COLOR)

    pygame.display.update()
