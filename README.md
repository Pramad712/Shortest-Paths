# Shortest Paths with A*
This application finds the shortest path on a grid between two nodes given by the user. The user also puts walls/obstacles which the path can not go through (but can go between ...).

## Dependencies (latest version as of when this project was created)
### • Python 3.10

### • Pygame 2.1 to make the GUI.

## Bugs and Issues
### • Since A* uses hueristics, *the true shortest path is not guaranteed*. For example, Google Maps does not always output the fastest route to your destination, especially when you are traveling long distances. You have to use your personal experience.

### • All other bugs and issues would be due to one of my dependencies. For example, pygame sometimes does not display the path even though the display is updated and the x and y coordinates are in bounds. It may even freeze the screen.

### • Since python (and pygame) are slow, if you move your mouse too fast when drawing the walls, not all squares will be drawn in gold.

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

### Length: The first phrase is "Path Found!" or "No Path Found" depending on if there is a path between the two nodes. If there one, then the next phrase will be in the form {cardinal movement count} + {intercardinal movement count}{diagonal distance = √2} ≈ {total distance rounded to the nearest thousandth}. Note that moving one unit in a cardinal direction is one unit, and the square root of two units for moving one unit intercardinally.

## Improvements
### • Use better hueristics to increase accuracy
### • Note: Edits have been and will be made over time, first upload was on August 16, 2022.
