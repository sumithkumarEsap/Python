import urllib.request
import requests
from bs4 import BeautifulSoup
import  os

my_list=[] #used to store the links

my_link="https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
link=requests.get(my_link)

obj=BeautifulSoup(link.content,"html.parser")
 #print the title of the webpage
print(obj.title)
#adding all the 'a' to the list
my_list.append(obj.find_all('a'))

#goes through each  'a' to get the reference
for i in obj.find_all('a'):
    print(i.get('href'))

#c=finds the table and prints the table data.
table = obj.find("table", { "class" : "wikitable sortable plainrowheaders" })
for row in table.findAll("tr"):
    cells = row.findAll("td")
    headings=row.findAll("th")
    print(cells,headings)