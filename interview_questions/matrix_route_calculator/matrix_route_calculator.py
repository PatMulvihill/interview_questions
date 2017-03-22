import random
import numpy as np
w = 3
h = 3
#populate grid with edge cost values
matrix = [[0 for x in range(w)] for y in range(h)]
for i in range(w):
    for j in range(h):
        matrix[i][j] = random.randint(0, 5)
print(np.matrix(matrix))

