import numpy as np

n = 5
print(np.arange(0, 10))  # allows us to make an array using numpy
print('\n')
print(np.zeros((3, 3)))  # makes a array of zeroes ( can be done with any number )
print('\n')
print(np.linspace(0, 100, 5))  # finds evenly spaced points between 2 points
print('\n')
print(np.eye(n))  # creates a 2 dimensional square matrix of size n
print('\n')
arr = (np.random.randint(1, 100, 25))  # returns a value of n random integers from 1 to 100
print('\n')
print(arr.reshape(5, 5))  # reshapes the array into a 5,5 grid
print('\n')
print(arr.max())  # finds the largest number in the array 'arr' it is the same for minimum
print('\n')
print(arr.argmax())  # finds the largest index location same for min
print('\n')
print(arr.shape)  # finds the dimensions of the array 'arr'
print('\n')
arr = (arr.reshape(25))  # changes the shape/dimensions of the array 'arr'
print(arr)
print('\n')
# indexing in numpy is just like normal python and also slice notation is used ex arr[2:8]
arr[:5] = 100  # setting values frm 0 to 5 = to 100
print(arr)
arr = arr.reshape(5, 5)
print('\n')
print(arr)
print('\n')
# try to use this notation it is less prone to error
print(arr[:, 0])
print('\n')
arr = (arr.reshape(25))
print(arr > 50)  # checks if each value is above '50' or not
boolarr = arr > 50
print(arr[boolarr])  # it has values of only true instances 'above 50'
print('\n')
print('\n')
# OPERATIONS
arr2 = np.arange(1, 10)
print(arr2 + arr2)  # it matches the indexes and then adds subtracts.. etc
print('\n')
print(arr2 - arr2)
print('\n')
print(arr2 * arr2)
print('\n')
print(arr2 ** 2)
print('\n')
print(arr2 - 50)  # it subtracts 50 to each value in the array
