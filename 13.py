import numpy as np

arr = np.random.randn(3, 5)
print("Array: " + str(arr))
print("Sum of elements: " + str(arr.sum()))
print("Min: " + str(arr.min()))
print("Max: " + str(arr.max()))
print("Min elements in every row: " + str(arr.min(axis=1)))
print("Min elements in every column: " + str(arr.min(axis=0)))
print("Max elements in every row: " + str(arr.max(axis=1)))
print("Max elements in every column: " + str(arr.max(axis=0)))
print("Index of min element: " + str(np.argmin(arr)))
print("Index of max element: " + str(np.argmax(arr)))
