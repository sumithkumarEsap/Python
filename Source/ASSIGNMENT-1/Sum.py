listt = [-1,-2,-3,1,2,3,-2,2,-1,1]
my_list = []
x = 0 #intialising the counter,
#running a loop for elements in listt
for i in range(len(listt)):
    k = i + 1
    #running a loop for the elements in list form 1st elem
    for j in range(k, len(listt) - 1):
        #checks if the sum of three digits is equal to o,if o it will add them to the group by making them into a tuple
        if (listt[k - 1] + listt[j] + listt[j + 1]) == 0:
            group = (listt[k - 1], listt[j], listt[j + 1])
            my_list.insert(x, group)
            x += 1

print(my_list)