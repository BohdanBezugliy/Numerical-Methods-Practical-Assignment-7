import numpy as np

arr = np.random.randn(4, 3)
print("Array: " + str(arr))
print("Avarage: " + str(arr.mean()))
print("Avarage elements in every row: " + str(arr.mean(axis=1)))
print("Avarage elements in every column: " + str(arr.mean(axis=0)))
