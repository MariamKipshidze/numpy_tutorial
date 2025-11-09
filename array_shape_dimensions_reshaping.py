import numpy as np

arr = np.arange(12)
print(arr.shape)
reshaped = arr.reshape(3, 4)
print(reshaped.shape)
flattened = reshaped.flatten()
