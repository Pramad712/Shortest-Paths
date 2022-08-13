from math import sqrt
import pygame

LENGTH, HEIGHT = 810, 800

LEFT_OFFSET, RIGHT_OFFSET = 5, 5
BOTTOM_OFFSET, TOP_OFFSET = 50, 50

GRAPH_LENGTH, GRAPH_HEIGHT = 40, 35
DIAGONAL_LENGTH = sqrt(2)

NODE_LENGTH, NODE_HEIGHT = (LENGTH - LEFT_OFFSET - RIGHT_OFFSET) // GRAPH_LENGTH, (HEIGHT - TOP_OFFSET - BOTTOM_OFFSET)\
                                                                                   // GRAPH_HEIGHT

BUTTON_LENGTH, BUTTON_HEIGHT = 120, 32

EMPTY_COLOR = (0, 0, 0)
CELL_COLOR = (0, 0, 0) # Cyan
WALL_COLOR = (255, 91, 35)  # Neon Orange
START_COLOR, END_COLOR = (0, 255, 0), (255, 0, 0)  # Green and Red respectively

BORDER_COLOR = (255, 255, 255)  # White

BUTTON_COLOR = (255, 0, 0) # Also Red
TEXT_COLOR = (255, 255, 255)  # White

PATH_COLOR = (0, 0, 255)

pygame.font.init()

FONT = pygame.font.SysFont("comicsans", 30)
