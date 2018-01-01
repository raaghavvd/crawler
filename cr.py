'''
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
'''
#Import the required modules
from twython import Twython
import json
import csv
import datetime

#Set parameters
keyword = 'Trump' #The desired keyword(s)
tweetsXiteration = 100 #Where 100 is the max
yesterday = datetime.datetime.now() - datetime.timedelta(days = 2)

dateFrom = datetime.datetime.today().strftime('%Y-%m-%d')
 #Inclusive (YYYY-MM-DD)
dateTo = yesterday.strftime('%Y-%m-%d') #Exclusive (YYYY-MM-DD)
done = False; #Must be false

#Setting the OAuth
Consumer_Key = 'cQqTiW9m7TuX9JYwCJVjpnhLQ'
Consumer_Secret = 'oElX55rEZoDWa9hflU0SRk6JlbzlBtIJLlIE96dBoPunzrG4XV'
Access_Token = '35775665-RtraC7pm3bD0EUtdej0YYw03o0DETpwkN7kyZQ7pL'
Access_Token_Secret = 'o1NtrzIoj0QaOdN9xTVyaKsboANjJqOpOFcgjHTLmYkWh'

#Connection established with Twitter API v1.1
twitter = Twython(Consumer_Key, Consumer_Secret, Access_Token, Access_Token_Secret)

#Twitter is queried
response = twitter.search(q = keyword, count = tweetsXiteration, since = dateFrom, until = dateTo, result_type = 'mixed')

#Results (partial)
countTweets = len(response['statuses'])

#If all the tweets have been fetched, then we are done
if not ('next_results' in response['search_metadata']):
    done = True

#If not all the tweets have been fetched, then...
while (done == False):

    #Parsing information for maxID
    parse1 = response['search_metadata']['next_results'].split("&")
    parse2 = parse1[0].split("?max_id=")
    parse3 = parse2[1]
    maxID = parse3

    #Twitter is queried (again, this time with the addition of 'max_id')
    response = twitter.search(q = keyword, count = tweetsXiteration, since = dateFrom, until = dateTo, max_id = maxID, include_entities = 1, result_type = 'mixed')

    #Updating the total amount of tweets fetched
    countTweets = countTweets + len(response['statuses'])

    #If all the tweets have been fetched, then we are done
    if not ('next_results' in response['search_metadata']):
        done = True

print(countTweets)
