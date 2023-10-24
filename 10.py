import numpy as np

countElements = np.random.randint(5)
c = np.random.randint(20, size=countElements)
d = np.random.randint(20, size=countElements)
print("c: " + str(c))
print("d: " + str(d))
print("c-d: " + str(c - d))
print("c+d: " + str(c + d))
print("c**2: " + str(c ** 2))
print("d**2: " + str(d ** 2))
print("c*d: " + str(c * d))
print("c/d: " + str(c / d))
print("c**d: " + str(c ** d))
