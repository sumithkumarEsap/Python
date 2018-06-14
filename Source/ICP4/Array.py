import numpy as np
x = np.random.random((10,10))
#printing the original array
print("Original Array:{}".format(x))

for i in x:
    #going through each array and prints minimum and maximum values in each array
    print("{} {}".format(i.min(),i.max()))
