import urllib.request, json
from bs4 import BeautifulSoup
import requests

'''
Parsing the articles
url="http://edition.cnn.com/2017/12/30/middleeast/iran-protests-intl/index.html"
r= requests.get( url)
data=r.text
soup=BeautifulSoup(data,'html.parser')
b=soup.find_all("p",class_="zn-body__paragraph speakable")
d=soup.find_all("div",class_="zn-body__paragraph")
print(d)
print(b)
'''
#This code is a webcrawler to fetch the articles from CNN related to Donald Trump
url_set=[]   #Initialises empty list to store all the urls from the CNN website of the articles related to Donald Trump
headline_set=[] #Initialises empty list to store all the headlines from the CNN website of the articles related to Donald Trump

def append_links(val,page):
    #FUNCTION TO HELP US FETCH THE INFORMATION OF THE URLs and HEADLINES iterating through 3 pages

    i=0
    with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10&from="+str(val)+"&page="+str(page)) as url:
        data_page = json.loads(url.read().decode())   #stores the json data generated

        while i<10:
            url_set.append(data_page['result'][i]['url'])  #fetches the URLand appends it to the list
            headline_set.append(data_page['result'][i]['headline'])#fetches the headlineand appends it to the list
            i=i+1
    #print(url_set)
    #print(headline_set)

pages=[1,2,3]
number_of_articles=[0,10,20]
for number,page_val in zip(number_of_articles,pages):
    append_links(number,page_val)  #calls the function

#print(len(url_set))
#print(len(headline_set))


#Parsing data
