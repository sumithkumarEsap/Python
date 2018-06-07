f = open("data.txt", "r")
for x in f:

   s=x
   length= len(x)
   count=0
   for i in range(length):

       if s[i] == " ":
           count += 1
       i+=1
   print(x[:-1]+","+str(count+1))
