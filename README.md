# Shortest Paths
Finds the shortest path on a grid between two nodes (given by the user). The user also puts obstacles which the path must not go through (but can go in between to walls ...).

# Dependencies
• Python 3.10
• Pygame 2.1.3dev4 to make the GUI.

# Known Bugs
• Since my code uses the A* Pathfinding Algorithm which involves hueristics, it sometimes gives paths that are very close to being optimal. Only one out of ~twenty-five times it gives dumb solutions, but only on completely random graphs.
• All other bugs would be due to one of my dependencies (I didn't find any of these before).

# Example Solve
![pathfinding_algorithms_project_example_solve](https://user-images.githubusercontent.com/77818951/185001752-8ae6cc3c-aaba-40ed-8c2d-2783c7da71aa.png)

Key:
Green: Start Position

Red: End Position

Gold: Wall

Orange: Nodes that the program processed, but it thinks they aren't in the shortest path.

Blue: Nodes that are in the shortest path.

Length: A decimal/integer that shows the distance between the shortest path between the start and end nodes that avoids the walls. Going a step north, east, south, or west has a distance of one, while going 1 unit north-east, north-west, south-east, or south-west has a cost of sqrt(2).
