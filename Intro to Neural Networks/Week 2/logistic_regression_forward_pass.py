import numpy as np

# Create a dummy dataset
x = np.random.random((10, 100))

# Initialize weights
w = np.random.random((10, 1))

# Bias term
b = 10

# Make sure the sizes are correct
print(f'The shape of the dataset is: {x.shape}\nThe shape of weights is: {w.shape}')
print(f'The shape of the transposed dataset is: {np.transpose(x).shape}')
z = np.dot(np.transpose(w), x) + b
print(f'The shape of z is: {z.shape}')
print(f'Z is :\n{z}')
