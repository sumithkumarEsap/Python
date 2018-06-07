list=["PHP", "Exercises", "Backend","Data"]
i=0
word_len=[]
for i in range(len(list)):
    listex=()
    listex=(len(list[i]),list[i])
    print(listex)
    word_len.insert(i,listex)
    i+=1
word_len.sort()
print(word_len[-1])
