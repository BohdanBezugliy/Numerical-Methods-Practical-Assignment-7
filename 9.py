import numpy as np


def fi(i, j):
    return i + 4 * j


arr = np.fromfunction(fi, (4, 5))
print("Array: " + str(arr))
