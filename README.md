# Shortest Paths with A*
Finds the shortest path on a grid between two nodes (given by the user). The user also puts walls which the path must not go through (but can go in between to walls ...).

## Dependencies
### • Python 3.10

### • Pygame 2.1 to make the GUI.

# Bugs and Issues
### • Since A* uses hueristics, **it does not guarantee the shortest path**. 

### • All other bugs and issues would be due to one of my dependencies (I didn't find any of these before).

# Example Solve
<img width="607" alt="image" src="https://user-images.githubusercontent.com/77818951/188323336-15f172a7-cf31-4e22-93c4-c634a45b8970.png">


## Key:

### Green: Start Position

### Red: End Position

### Gold: Wall

### Orange: Nodes that the program processed, but it thinks they aren't in the shortest path.

### Blue: Nodes that are in the shortest path.

### Length: A decimal/integer that shows the distance between the shortest path between the start and end nodes that avoids the walls. Going one unit north, east, south, or west has a distance of one, but going one unit north-east, north-west, south-east, or south-west has a cost of sqrt(2).

# Improvements
### • Use better hueristics to increase accuracy
