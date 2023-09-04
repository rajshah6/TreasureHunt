import random
import time

def create_grid():
    grid = []
    for row in range(12):
        grid.append(["."]*12)
    return grid

def display_grid(grid):
    for row in grid:
        print(" ".join(row))

def get_pos(location_y, location_x, prompt):
    while True:
        pos = input(prompt).lower()
        if pos == "n":
            location_y -= 1
            return location_y, location_x
        if pos == "s":
            location_y += 1
            return location_y, location_x
        if pos == "e":
            location_x += 1
            return location_y, location_x
        if pos == "w":
            location_x -= 1
            return location_y, location_x

while True:
    grid = create_grid()

    start_time = time.time()

    for treasure in range(3):
        grid[random.randint(0,11)][random.randint(0,11)] = "$"

    location_y = len(grid)-1
    location_x = 0
    steps = -1

    while True:
        steps += 1

        if grid[location_y][location_x] == "$":
           end_time = time.time()
           print(f"Congratulations! You won the treasure. It took you {steps} steps and {end_time-start_time} seconds to reach it!\n")
           break

        grid[location_y][location_x] = "P"
        display_grid(grid)

        grid[location_y][location_x] = "."
        
        temp_y, temp_x = get_pos(location_y, location_x, "Enter direction (N, E, S, W): ")

        while temp_y < 0 or temp_y > 11 or temp_x < 0 or temp_x > 11:
            temp_y, temp_x = get_pos(location_y, location_x, "Player out of grid! Enter direction (N, E, S, W): ")

        location_y, location_x = temp_y, temp_x

    play_again = input("Would you like to play again? (y/n): ")
    if play_again != "y":
        print("Thanks for playing!")
        break
