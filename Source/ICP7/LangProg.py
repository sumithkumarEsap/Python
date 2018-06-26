import urllib.request
import requests
from bs4 import BeautifulSoup
import  os
import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk import ne_chunk, pos_tag, word_tokenize
from nltk.tree import Tree
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags

my_link="https://en.wikipedia.org/wiki/Python_(programming_language)"
link=requests.get(my_link)

soup=BeautifulSoup(link.content,"html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()
# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)
#print(text)

fp=open("Input.txt","w",encoding="utf-8")
fp.write(text)
fp.close()

#tokenization
file_content = open("Input.txt",encoding="utf-8").read()
tokens = nltk.word_tokenize(file_content)
#print (tokens)

#pos tagging
tokens_pos = pos_tag(tokens)
#print(tokens_pos )


#named entity recognition
named_entities = []
def NamedE():
    with open('Input.txt', 'r', encoding="utf-8") as f:
        for line in f:#for each line taking tokens and tagging pos and adding them to chunks
            ne_tree = ne_chunk(pos_tag(word_tokenize(line)))

            iob_tagged = tree2conlltags(ne_tree)
            named_entities.append(iob_tagged)
    print(named_entities)

def stemming_text_1():
    with open('Input.txt', 'r',encoding="utf-8") as f:
        for line in f:
            print (line)
            singles = []

            stemmer = PorterStemmer() #using PorterStemmer for stemming each words
            for plural in line.split():
                singles.append(stemmer.stem(plural))
            print (' '.join(singles))


def lemmatizing_text():
    with open('Input.txt', 'r', encoding="utf-8") as f:
        for line in f:
            print (line)
            singles = []

            lemmatizer = WordNetLemmatizer()
            for plural in line.split():#for rach line splitting the line int words and performing lemmatization
                singles.append(lemmatizer.lemmatize(plural))
            print (' '.join(singles))

def Ngrams():
    n = 3
    with open('Input.txt', 'r', encoding="utf-8") as f:
        for line in f:
            trigrams = ngrams(line.split(), n)
            for grams in trigrams:
                print(grams)


#lemmatizing_text()
#stemming_text_1()
#NamedE()
#Ngrams()
