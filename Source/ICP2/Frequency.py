f = open("data.txt", "r")
for x in f:
  s=len(x)
  #print(x[:-1]+","+str(s-1))
  r=open("new_data.txt","a")
  r.write(x[:-1]+","+str(s-1))
r.close()