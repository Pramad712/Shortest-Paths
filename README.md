# Shortest Paths with A*
This application finds the shortest path on a grid between two nodes given by the user. The user also puts walls/obstacles which the path can not go through (but can go between ...).

## Dependencies (latest version as of when this project was created)
### • Python 3.11

### • Pygame 2.1 to make the GUI.

## Bugs and Issues
### • Since python (and pygame) are slow, if you move your mouse too fast when drawing the walls, not all squares will be drawn in gold.
### • If you find any other problems or know how to fix one of these issues, please put your comments in the issues page or submit a pull request.

# How to play
First, choose a start and end node by clicking on two unique cells of the 40x35 grid. Draw some walls/obstacles on the grid, pressing the "d" key on your keyboard to change from "draw" to "delete" mode or vice versa. When finished, press the "Done" button at the bottom of the screen. The application will find the shortest path between the start and end cells marked as shown below. It may take a few seconds because it uses a slow computation to simplify the path. Press the "Restart" button if you want to play again, or exit by pressing the "X" button on the top-right corner of your screen.

# Example Solve
<img width="810" alt="Screenshot 2023-08-04 at 4 34 06 PM" src="https://github.com/Pramad712/Shortest-Paths/assets/77818951/837fcc01-c407-4ccc-86f9-ad9ffcb1c957">

## Key:

### Green: Start Cell

### Red: End Cell

### Gold: Walls

### Orange: Nodes that the program processed, but aren't in the shortest path.

### Blue: Nodes that are in the shortest path.

### Length: The first phrase is "Path Found!" or "No Path Found" depending on if there is a path between the two nodes. If there one, then the next phrase will be in the form {cardinal distance} + {intercardinal movements}{diagonal distance = √2} ≈ {distance rounded to the nearest thousandth}. Note that moving one unit in a cardinal direction is one unit, and the square root of two units for moving one unit intercardinally.

## Edit History
### • August 16, 2022: First release, with a few bugs and doesn't guarantee the shortest path due to a recursive backtracking-like approach.
### • Until next release: Many bug fixes
### • August 4, 2023: An iterative approach is implemented using a priority queue and guarentees the shortest path. However, since the original approach picked the node that will minimize the heuristic and never looked back (unless if no path was found), the new approach is usually slower by at most a couple seconds. The output format also changed (see the key above).
### • October 21, 2023: An insane performance improvement on very complicated inputs is done by implementing a set that stores all visited nodes. This prevents cycles by making sure the same node isn't processed. An small wait time is added so the user can see the order of the nodes processed in complicated graphs.
