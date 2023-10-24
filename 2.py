import numpy as np

arr = np.random.randint(20, size=(2, 3))
print("Array: " + str(arr))
arrComplex = arr.astype("complex")
print("Complex array: " + str(arrComplex))
arrFloat = arr.astype("float")
print("Float array: " + str(arrFloat))
