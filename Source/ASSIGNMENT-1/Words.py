
def word_function(sen):
    wordlist = sen.split()
    a = len(wordlist)
    largest_word = " "
    #checking if the length of the sentence is even
    #if not even then we can say that the middle word will exactly half way
    #else it will be two words
    if a % 2 != 0:
        b = (a + 1) / 2
        print("middle word is :" + wordlist[int(b - 1)])
    else:
        b = a / 2
        print("middle word is :" + wordlist[int(b - 1)], wordlist[int(b)])


    for i in range(a):
        '''comparing empty string with the 1st string and assigning the string as largest one,this will be compared with the next word if its larget 
        then it will be assigned as the largest word        '''
        if len(largest_word) < len(wordlist[i]):
            largest_word = wordlist[i]

    print("Largest Word :{}".format(largest_word))

    #creating ana empty string to hold the reversed string
    strng = ''
    ra = []
    for i in range(len(wordlist)):
        word = wordlist[i][-1::-1]
        ra.append(word)
    #converting the list into string
    for i in ra:
        strng += " " + str(i)
    print("reverse string is:"+strng)



inp = input("enter a sentence:")
#calling the function by passing sentence as its input
word_function(inp)