import numpy as np

countRows = np.random.randint(10)
countColumns = np.random.randint(10)
c = np.random.randint(20, size=(countRows, countColumns))
d = np.random.randint(20, size=(countRows, countColumns))
print("c: " + str(c))
print("d: " + str(d))
print("c-d: " + str(c - d))
print("c+d: " + str(c + d))
print("c**2: " + str(c ** 2))
print("d**2: " + str(d ** 2))
print("c*d: " + str(c * d))
print("c/d: " + str(c / d))
print("c**d: " + str(c ** d))
