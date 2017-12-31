from bs4 import BeautifulSoup
import requests


url="https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
r= requests.get(url)
data=r.text
soup=BeautifulSoup(data,'html.parser')
tweets=[p.text for p in soup.findAll('p',class_='tweet-text')]
i=0
for tweet in tweets:
    i=i+1
    print(tweet)
    print("\n")
print(i)
