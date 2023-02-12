# Shortest Paths with A*
This application finds the shortest path on a grid between two nodes given by the user. The user also puts walls/obstacles which the path can not go through (but can go between ...).

## Dependencies (latest version as of when this project was created)
### • Python 3.10

### • Pygame 2.1 to make the GUI.

## Bugs and Issues
### • Since A* uses hueristics, *it does not 100% guarantee the shortest path, however it may be close to the correct one*. 

### • All other bugs and issues would be due to one of my dependencies. For example, pygame sometimes does not display the path even though the display is updated and the x and y coordinates are in bounds. It may even freeze the screen.

### • Since python (and pygame) are slow, if you move your mouse too fast when drawing the walls, not all squares will be drawn in gold.

# How to play
First, choose a start and end node by clicking on two unique cells of the 40x35 grid. Draw some walls/obstacles on the grid, pressing the "d" key on your keyboard to change from "draw" to "delete" mode or vice versa. When finished, press the "Done" button at the bottom of the screen. The application will find the shortest path between the start and end cells marked as shown below. It may take a few seconds because it uses a slow computation to simplify the path. Press the "Restart" button if you want to play again, or exit by pressing the "X" button on the top-right corner of your screen.

# Example Solve
![pathfinding_algorithms_project_example_solve](https://user-images.githubusercontent.com/77818951/210642450-f8232aff-7005-4a3c-8ef6-2e218d491095.png)

## Key:

### Green: Start Cell

### Red: End Cell

### Gold: Walls

### Orange: Nodes that the program processed, but aren't in the shortest path.

### Blue: Nodes that are in the shortest path.

### Length: A decimal/integer that shows the size of the shortest path between the start and end nodes. Going one unit in a cardinal direction has a distance of one, but going one unit intercardinally has a cost of sqrt(2) (1.4142135623730951 according to python).

## Improvements
### • Use better hueristics to increase accuracy
### • Note: Edits have been and will be made over time, first upload was on August 16, 2022.
