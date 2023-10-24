import numpy as np

arr = np.random.randn(9)
print("Array: " + str(arr))
print("Cumulative sums of elements: " + str(np.cumsum(arr)))
print("Cumulative products of elements: " + str(np.cumprod(arr)))
