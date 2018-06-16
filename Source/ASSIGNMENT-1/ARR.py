import numpy as np
a = np.random.randint(1,20,15)
print("Original array:")
print(a)
s = sorted(a) # Sorting the array
print(s)
x = 0 # initializing the reference value
c = 1
d = {}
for i in s:   #loop for iterating items in s
    j = i+1
    c = 0
    for j in s:   #Anothe loop for comparing one element with rest
        if (i == j):
            c = c + 1  #incrementing the count if same number occurs
    if (c >= x): # storing values to the dictionary by taking x as reference
        x = c
        d[i] = c

print(d)
dic = sorted(d) #sorting the updated dictionary
c = dic[-1]

print("most frequent numbers are:%d" %c)
