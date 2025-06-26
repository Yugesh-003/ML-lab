
import numpy as np
arr = np.array([[1,3,5,7],
                [3,3,4,5]])
x = -2
newarr1 = arr.reshape(1,8)
newarr = arr.reshape(x) 

print(newarr1.shape)
print(newarr.shape)

print(x)