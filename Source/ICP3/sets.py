usr_inp=input("enter your sentence")
c=0
set={'a','e','i','o','u'}
for i in usr_inp:
    for j in set:
        if(i==j):
            c+=1


print(c)
