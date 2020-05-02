import pandas as pd
import numpy as np

# NumPy practice

n1 = np.array([1, 2, 3, ])
print(n1)

n2 = np.array([[1, 2, 3], [4, 5, 6]])
print(n2)

n3 = np.zeros((2, 3))
print(n3)

print(type(n1))

n4 = np.full((2, 3), 5)
print(n4)

n5 = np.arange(10, 30, 5)
print(n5)

n6 = np.arange(20, 10, -2)
print(n6)

n7 = np.random.randint(1, 200, 10)
print(n7)

a = np.array([20, 10,5])
b = np.array([30, 40,15])

print(a)
print(b)

print("Sum: " + str(np.sum([a, b])))
print("axis 0 sum:" + str(np.sum([a,b],axis=0)))
print("axis 1 sum:" + str(np.sum([a,b],axis=1)))
print("vstack:" + str(np.vstack([a,b])))
print("hstack:" + str(np.hstack([a,b])))
print("column stack:" + str(np.column_stack([a,b])))