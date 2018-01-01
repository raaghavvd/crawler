from flask import Flask, render_template,request
from bs4 import BeautifulSoup
import requests
import urllib.request, json
from TwitterAPI import TwitterAPI



app=Flask(__name__) #Creation of flask app
@app.route('/')
def index():
    #return render_template("home.html") #returns homepage
    return render_template("index.html") #returns homepage

@app.route("/Twitter.html",methods=["GET"]) #Fetches the twitter page


def Twitter():
    '''
    The web crawler from tweets.py has been implemented here
    '''
    if request.method =='GET':
        url="https://twitter.com/realDonaldTrump?ref_src=twsrc%5Egoogle%7Ctwcamp%5Eserp%7Ctwgr%5Eauthor"
        r= requests.get(url)
        data=r.text
        soup=BeautifulSoup(data,'html.parser')
        tweets=[p.text for p in soup.findAll('p',class_='tweet-text')]
        print(tweets)
        return render_template("Twitter.html",items= tweets)

@app.route("/Articles.html",methods=["GET"]) # Fetches Articles from CNN which are related to Donald Trump
def Articles():

    '''
    The Webcrawler from CNN.py has been implemented here to help us get the data
    '''

    if request.method =='GET':

        url_set=[]
        headline_set=[]


        def append_links(val,page):
            i=0
            with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10&from="+str(val)+"&page="+str(page)) as url:
                data_page = json.loads(url.read().decode())


            while i < 10:

                    url_set.append(data_page['result'][i]['url'])
                    headline_set.append(data_page['result'][i]['headline'])
                    i=i+1
            #print(url_set)
            #print(headline_set)

        pages=[1,2,3]
        number_of_articles=[0,10,20]
        for number,page_val in zip(number_of_articles,pages):
            append_links(number,page_val)
        return render_template("Articles.html",items= headline_set, urls=url_set) #returns the headlines to Articles page


@app.route("/Tweets.html",methods=["GET"])
def Tweets():
    tweet_list=[]
    API_KEY = 'cQqTiW9m7TuX9JYwCJVjpnhLQ'
    API_SECRET = 'oElX55rEZoDWa9hflU0SRk6JlbzlBtIJLlIE96dBoPunzrG4XV'
    ACCESS_TOKEN = '35775665-RtraC7pm3bD0EUtdej0YYw03o0DETpwkN7kyZQ7pL'
    ACCESS_TOKEN_SECRET= 'o1NtrzIoj0QaOdN9xTVyaKsboANjJqOpOFcgjHTLmYkWh'

    #Making the Connection with the API
    api = TwitterAPI(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    count = 0
    r = api.request('statuses/filter', {'track':'Donald Trump'})

    #The following loop generates the latest 20 tweets containing 'Donald Trump'

    for item in r:
         tweet_list.append(item['text'])
         count=count+1
         if count > 19:
             break
    return render_template("Tweets.html", items= tweet_list)  #Returns the list of the latest tweets to the website





if __name__=="__main__":
    app.run(debug=True) #Runs the app
