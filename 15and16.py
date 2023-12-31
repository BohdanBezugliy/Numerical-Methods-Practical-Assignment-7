import numpy as np

a = np.random.randn(12)
b = np.random.randn(12)
print("15)")
print("Array a: " + str(a))
print("Array b: " + str(b))
print("Element-by-element maximum: " + str(np.maximum(a, b)))
print("Element-by-element minimum: " + str(np.minimum(a, b)))
print("16)")
print("Array a: " + str(a))
absolute = np.fabs(a)
print("Absolute value in new array: " + str(absolute))
square = a ** 2
print("Square value in new array: " + str(square))
exponent = np.exp(a)
print("Exponent value in new array: " + str(exponent))
sin = np.sin(a)
print("Sin value in new array: " + str(sin))
sign = np.sign(a)
print("Sing value in new array: " + str(sign))
IntAndFract = np.modf(a)
print("Integers and fractional values: " + str(IntAndFract))
