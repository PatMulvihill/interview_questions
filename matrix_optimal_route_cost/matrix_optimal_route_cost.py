# Given a matrix of size w * h, where w = 3 and h = 3 like so:
#   [5 3 2]
#   [2 0 5]
#   [0 4 2]
# Calculate the optimal (lowest cost) route you can take to get from (0, 0) (top left corner)
# to (w - 1, h - 1) (bottom right corner). Each step taken can either be a step to the right (x + 1)
# or a step down (y + 1).  You cannot backtrack.

import random
import numpy as np
X = 5
Y = 5
# declare grid variable which represents our matrix, initialize it with 0's
grid = [[random.randint(0, 5) for y in range(Y)] for x in range(X)]
# create a routes matrix of the same size as grid that will store the amount
# of routes possible at each index
costs = [[0 for y in range(Y)] for x in range(X)]
print("Starting Grid:")
print(np.matrix(grid))
print("\nRoutes Matrix:")
print(np.matrix(routes))
