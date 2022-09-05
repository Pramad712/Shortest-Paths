# Shortest Paths with A*
This application finds the shortest path on a grid between two nodes given by the user. The user also puts walls/obstacles which the path can not go through (but can go in between them ...).

## Dependencies
### • Python 3.10

### • Pygame 2.1 to make the GUI.

# Bugs and Issues
### • Since A* uses hueristics, **it does not guarantee the shortest path**. 

### • All other bugs and issues would be due to one of my dependencies (I didn't find any of these before).

# How to play
First, you choose a start node by clicking on a cell of the 40x35 grid. Then choose the end node other than the start. Finally, you draw some walls/obstacles on the grid. If you make a mistake, then click on the "d" key on your keyboard to enter delete mode. Click on any cell that is a wall, and it would be replaced by an empty cell; click on the "d" key again to enter draw mode. When you are done, press the "Done" button at the bottom of the screen. The application will find the shortest path between the start and end cells, and mark it as shown below. It may take a few seconds because it uses a slow computation to simplify the path. After that, you may press the "Restart" button.

# Example Solve
<img width="607" alt="image" src="https://user-images.githubusercontent.com/77818951/188323336-15f172a7-cf31-4e22-93c4-c634a45b8970.png">

## Key:

### Green: Start Cell

### Red: End Cell

### Gold: Walls

### Orange: Nodes that the program processed, but aren't in the shortest path.

### Blue: Nodes that are in the shortest path.

### Length: A decimal/integer that shows the size of the shortest path between the start and end nodes. Going in a cardinal direction one unit has a distance of one, but going one unit intercardinally has a cost of sqrt(2).

# Improvements
### • Use better hueristics to increase accuracy
