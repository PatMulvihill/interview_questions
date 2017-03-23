# Given a matrix of size w * h, where w = 3 and h = 3 like so:
#   [5 3 2]
#   [2 0 5]
#   [0 4 2]
# Calculate the total number of routes you can take to get from (0, 0) (top left corner)
# to (w, h) (bottom right corner). Each step taken can either be a step to the right (x + 1)
# or a step down (y + 1).  You cannot backtrack.


import random
import numpy as np
w = 10
h = 10
# declare grid variable which represents our matrix
grid = [[0 for x in range(w)] for y in range(h)]
# create a routes matrix of the same size as grid that will store the amount
# of routes possible at each index
routes = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        # initalise grid matrix with random values (which don't matter in this problem)
        grid[i][j] = random.randint(0, 5)
        # initialise routes matrix with values of 0 so that we can effectively index in
        routes[i][j] = 0
print("Starting Grid:")
print(np.matrix(grid))
print("\nRoutes Matrix:")
print(np.matrix(routes))
# Initalise the top and left edge route values to 1
# There will always only be 1 way to get to any of these values because of the
# no back-tracking condition and the condition that steps much only be downward
# or rightward.
for i in range(w):
    for j in range(h):
        if i==0 or j == 0:
            routes[i][j] = 1
        else:
            routes[i][j] = routes[i - 1][j] + routes[i][j-1]
print("\nOnce all the routes have been calculated, our routes matrix looks like this.")
print(np.matrix(routes))
print("\nThe total number of routes will be contained in the [w-1][h-1] index.")
print("The total number of routes possible is", routes[w - 1][h - 1])
