import pygame
from graph import *
from a_star import solve

def main():
    while True:
        window = pygame.display.set_mode((LENGTH, HEIGHT))
        window.fill(EMPTY_COLOR)
        pygame.display.set_caption("Shortest Paths Using A*")

        graph = create_graph()
        draw_graph(window, graph)

        write_instruction(window, "Click on the Start Position", "start")
        start_node = None

        while start_node is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if LEFT_OFFSET + 1 < x < LENGTH - RIGHT_OFFSET and TOP_OFFSET + 1 < y < HEIGHT - BOTTOM_OFFSET:
                        row, column = (y - TOP_OFFSET) // NODE_HEIGHT, (x - LEFT_OFFSET) // NODE_LENGTH

                        start_node = graph[row][column]
                        graph[row][column].type = "start"

                        break

            draw_graph(window, graph)

        write_instruction(window, "Click on the End Position", "end")
        end_node = None

        while end_node is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos

                    if LEFT_OFFSET + 1 < x < LENGTH - RIGHT_OFFSET and TOP_OFFSET + 1 < y < HEIGHT - BOTTOM_OFFSET:
                        row, column = (y - TOP_OFFSET) // NODE_HEIGHT, (x - LEFT_OFFSET) // NODE_LENGTH

                        if graph[row][column].type != "start":
                            end_node = graph[row][column]
                            graph[row][column].type = "end"

                            break

            draw_graph(window, graph)

        button = draw_button(window, "Done!")

        write_instruction(window, "Draw the Walls", "wall")
        done, mouse_motion_on, draw = False, False, True

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                    draw = not draw

                elif event.type == pygame.MOUSEBUTTONDOWN or mouse_motion_on and event.type == pygame.MOUSEMOTION:
                    x, y = event.pos

                    if LEFT_OFFSET + 1 < x < LENGTH - RIGHT_OFFSET and TOP_OFFSET + 1 < y < HEIGHT - BOTTOM_OFFSET:
                        row, column = (y - TOP_OFFSET) // NODE_HEIGHT, (x - LEFT_OFFSET) // NODE_LENGTH

                        if draw and graph[row][column].type not in ["start", "end"]:
                            graph[row][column].type = "wall"

                        if not draw and graph[row][column].type == "wall":
                            graph[row][column].type = "cell"

                    mouse_motion_on = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos

                    if button.left <= x <= button.left + button.width and button.top <= y <= button.top + button.height:
                        done = True
                        break

                    else:
                        # After you let go of your mouse, you have to click again to draw the streak of walls
                        mouse_motion_on = False

            draw_graph(window, graph)

        clear_button(window)

        path = solve(window, graph, start_node, end_node)

        if path == "INVALID":
            write_instruction(window, "No Path Found")

        else:
            write_instruction(window, f"Path Found! Length: {path[1]}")
            draw_path(window, path)

        button = draw_button(window, "Restart")
        done = False

        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                elif event.type == pygame.MOUSEBUTTONUP:
                    x, y = event.pos

                    if button.left <= x <= button.left + button.width and button.top <= y <= button.top + button.height:
                        done = True
                        break

if __name__ == "__main__":
    main()
