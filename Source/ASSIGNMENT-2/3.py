from __future__ import division
import nltk, re, pprint
import re, collections
from nltk import pos_tag, ne_chunk, ngrams

f=open('data.txt')
raw=f.read().lower()
f=open('data.txt')
raw_lines=f.readlines()

from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(raw)

# lemmatization
wnl = nltk.WordNetLemmatizer()
lem_txt=[wnl.lemmatize(t) for t in tokens]
print('Lemmatization')
print(lem_txt)
print('----------------------------------------------------------')

# pos tagging
pos_txt=nltk.pos_tag(tokens)
print('After applying POS')
print(pos_txt)
print('------------------------------------------------------------------------')


verbs=[s[0] for s in pos_txt if s[1] == 'VB']
remaining_words=[s[0] for s in pos_txt if s[1] != 'VB']

# removing stop words such as 'the','is'
from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

filtered_words = [w for w in remaining_words if not w in stop_words]
print('After removing all the verbs')
print(filtered_words)
print('--------------------------------------------------------------------------')

f1 = open('bigram_1.txt','w')
for i in filtered_words :
    f1.write(i + ' ')
f1.close()

n = 2
with open('bigram_1.txt', 'r', encoding="utf-8") as f:
    for line in f:
        bigrams = ngrams(line.split(), n)
        for grams in bigrams:
            print (grams)

import nltk
f = open('bigram_1.txt','r')
raw = f.read()
tokens = nltk.word_tokenize(raw)


o_d=open("data.txt","r")
raw1 = o_d.read()
tokens1 = nltk.sent_tokenize(raw1)

#Create your bigrams
bgs = nltk.bigrams(tokens)

#compute frequency distribution for all the bigrams in the text
fdist = nltk.FreqDist(bgs)
for k,v in fdist.items():
    print (k,v)
#sorting the dict by items so that items with highest frequency will be at the last
sorted_by_value = sorted(fdist.items(), key=lambda kv: kv[1])
#storing the last five values from sorted dict i.ie., the top 5 words
top_5=dict((sorted_by_value[:-6:-1]))
print(top_5)
#creating the list to store top 5 sentences
l = []
for i in tokens1:
    #print(i)
    for k,v in top_5:
        if(k,v in i):
            l.append(i)
print(l)
file = open('top5_word_lines.txt','w')
#writing the top 5 sentences into the new file
for i in l:
    file.write(i)
file.close()