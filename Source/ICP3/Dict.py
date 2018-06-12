from collections import OrderedDict

def wordListToFreqDict(wordlist):
    wordfreq = [wordlist.count(p) for p in wordlist]
    my_dict= dict(zip(wordlist,wordfreq))
    return my_dict
#asks user for inpit
sen=input("enter your sentence")
#splitting the sentence using split()

words2 = sen.split( )
#creating the dictionary for the words and frequency
dict=wordListToFreqDict(words2)
print(dict)
#calling OrderedDict function on normal dict by items.
print(OrderedDict(sorted(dict.items(), key=lambda t: t[0])))