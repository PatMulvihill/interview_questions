# Given a matrix of size w * h, where w = 3 and h = 3 like so:
#   [5 3 2]
#   [2 0 5]
#   [0 4 2]
# Calculate the optimal (lowest cost) route you can take to get from (0, 0) (top left corner)
# to (w - 1, h - 1) (bottom right corner). Each step taken can either be a step to the right (x + 1)
# or a step down (y + 1).  You cannot backtrack.

import random
import numpy as np

X = 10 # width of matrix
Y = 10 # height of matrix

# declare grid variable which represents our matrix, initialize it with random numbers
grid = [[random.randint(1, 100) for y in range(Y)] for x in range(X)]
# create a costs matrix of the same size as grid that will store the minimum
# cost to get to each index in the matrix
costs = [[0 for y in range(Y)] for x in range(X)]
print("Starting Grid:")
print(np.matrix(grid))
print("\nCosts Matrix:")
print(np.matrix(costs))

# initialise the top and left edges of the matrix as those costs can only
# be achieved by only 1 route
for i in range(X):
    for j in range(Y):
        if i == 0 and j == 0:
            costs[i][j] = grid[i][i]
        elif i == 0:
            costs[i][j] = grid[i][j] + costs[i][j - 1]
        elif j==0:
            costs[i][j] = grid[i][j] + costs[i - 1][j]
        else:
            costs[i][j] = grid[i][j] + min(costs[i - 1][j], costs[i][j - 1])

print("\nOnce all the minimum costs have been calculated, our costs matrix looks like this.")
print(np.matrix(costs))
print("\nThe optimal(minimum) cost will be contained in the [X-1][Y-1] index.")
print("The optimal route cost is", costs[X - 1][Y - 1])
