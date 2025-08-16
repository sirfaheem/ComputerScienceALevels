import os
import time
import random

# Set the dimensions of the grid
WIDTH = 60
HEIGHT = 20

# Create an empty grid
grid = []
for i in range(HEIGHT):
    grid.append([])
    for j in range(WIDTH):
        grid[i].append(0)

# Set the initial state of the cells
for i in range(HEIGHT):
    for j in range(WIDTH):
        if random.randint(0, 100) < 20:
            grid[i][j] = 1

# Define the rules of the game
def update_grid():
    # Create a copy of the grid to use for reference
    new_grid = []
    for i in range(HEIGHT):
        new_grid.append([])
        for j in range(WIDTH):
            new_grid[i].append(grid[i][j])

    # Iterate over each cell in the grid
    for i in range(HEIGHT):
        for j in range(WIDTH):
            # Count the number of live neighbors
            live_neighbors = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    if x == 0 and y == 0:
                        continue
                    if i + x < 0 or i + x >= HEIGHT:
                        continue
                    if j + y < 0 or j + y >= WIDTH:
                        continue
                    if grid[i + x][j + y] == 1:
                        live_neighbors += 1

            # Apply the rules of the game
            if grid[i][j] == 0 and live_neighbors == 3:
                # A dead cell with three live neighbors becomes alive
                new_grid[i][j] = 1
            elif grid[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                # A live cell with fewer than two or more than three live neighbors dies
                new_grid[i][j] = 0

    # Update the grid
    for i in range(HEIGHT):
        for j in range(WIDTH):
            grid[i][j] = new_grid[i][j]

# Print the grid to the terminal
def print_grid():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if grid[i][j] == 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Main game loop
while True:
    # Clear the screen
    os.system("cls")

    # Update the grid and print it
    update_grid()
    print_grid()

    # Wait for a moment before updating again
    time.sleep(0.25)
