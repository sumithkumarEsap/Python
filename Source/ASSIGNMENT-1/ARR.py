import numpy as np
#creating 15 random values by using numpy rndom function in the range of 1,20



a = np.random.randint(1,20,15)
print("Original array:")
print(a)
unique_elements, counts_elements = np.unique(a, return_counts=True)
my_arr=[unique_elements],[counts_elements]
print(my_arr[0][1])

print("Frequency of unique values of the said array:")
print(np.asarray((unique_elements, counts_elements)))




'''
l=np.random.randint(1,20,15)
#adding these values to the list
my_list=list(l)
print(my_list)



count=0
new_list=[]
#creating a empty set to hold the repeating numbers
my_set={}
#print(list([x for x in my_list if my_list .count(x) > 1])[0]))
for x in my_list:
    if my_list.count(x)>1:
        new_list.append(x)
my_set=set(new_list)
print(my_set)
'''