from bs4 import BeautifulSoup
import requests
'''
This program is a webcrawler to fetch 20 tweets from Donald Trump's twitter account

'''

url="https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"   #Url of Donald Trump's Twitter account
r= requests.get(url) #fetch the data
data=r.text #generates and stores the text from the data
soup=BeautifulSoup(data,'html.parser') #BeautifulSoup parses
tweets=[p.text for p in soup.findAll('p',class_='tweet-text')]  #gets all the tweets



i=0
for tweet in tweets:  #prints each tweet from the list
    i=i+1
    print(tweet)
    print("\n")
print(i)
