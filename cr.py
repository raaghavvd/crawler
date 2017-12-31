from bs4 import BeautifulSoup
import requests

url="http://edition.cnn.com/2017/12/30/middleeast/iran-protests-intl/index.html"
r= requests.get( url)
data=r.text
soup=BeautifulSoup(data,'html.parser')
b=soup.find_all("p",class_="zn-body__paragraph speakable")
d=soup.find_all("div",class_="zn-body__paragraph")
print(d)
print(b)
