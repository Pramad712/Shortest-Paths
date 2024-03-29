from math import ceil, sqrt
import pygame

LENGTH, HEIGHT = 810, 800

LEFT_OFFSET, RIGHT_OFFSET = 5, 5
BOTTOM_OFFSET, TOP_OFFSET = 50, 50

GRAPH_LENGTH, GRAPH_HEIGHT = 40, 35
DIAGONAL_DISTANCE = sqrt(2)
DIAGONAL_DISTANCE_REPR = "√2"

NODE_LENGTH, NODE_HEIGHT = ceil((LENGTH - LEFT_OFFSET - RIGHT_OFFSET) / GRAPH_LENGTH), ceil((HEIGHT - TOP_OFFSET - BOTTOM_OFFSET) / GRAPH_HEIGHT)

BUTTON_LENGTH, BUTTON_HEIGHT = 120, 32

EMPTY_COLOR = (0, 0, 0) # Black
CELL_COLOR = (0, 0, 0)  # Black
WALL_COLOR = (255, 180, 40)  # Gold
START_COLOR, END_COLOR = (0, 255, 0), (255, 0, 0)  # Green and Red respectively

BORDER_COLOR = (255, 255, 255)  # White

BUTTON_COLOR = (255, 0, 0)  # Also Red
TEXT_COLOR = (255, 255, 255)  # White

PROCESSING_NODE_COLOR = (255, 140, 35) # Orange
PATH_COLOR = (0, 0, 255)  # Blue

pygame.font.init()

FONT = pygame.font.SysFont("comicsans", 30)
