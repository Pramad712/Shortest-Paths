# Shortest Paths
Finds the shortest path on a grid between two nodes (given by the user). The user also puts walls which the path must not go through (but can go in between to walls ...).

# Dependencies
• Python 3.10

• Pygame 2.1 to make the GUI.

# Bugs
• Since my code uses the A* pathfinding algorithm which involves hueristics, it sometimes gives paths that are very close to being optimal. 

• If there is no path, then the program would take a really long time to run. This is because it would have to brute-force all paths to find a working solution, becoming as slow as Djikstra's algorithm.

• All other bugs would be due to one of my dependencies (I didn't find any of these before).

# Example Solve
![pathfinding_algorithms_project_example_solve](https://user-images.githubusercontent.com/77818951/185023562-d0139cf4-325f-4aeb-aeee-ccfa5c2c8a71.png)


Key:
Green: Start Position

Red: End Position

Gold: Wall

Orange: Nodes that the program processed, but it thinks they aren't in the shortest path.

Blue: Nodes that are in the shortest path.

Length: A decimal/integer that shows the distance between the shortest path between the start and end nodes that avoids the walls. Going a step north, east, south, or west has a distance of one, but going 1 unit north-east, north-west, south-east, or south-west has a cost of sqrt(2).

# Improvements
• Use better hueristics to increase accuracy
