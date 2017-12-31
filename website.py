from flask import Flask, render_template,request
from bs4 import BeautifulSoup
import requests
import urllib.request, json


app=Flask(__name__) #Creation of flask app
@app.route('/')
def index():
    return render_template("home.html") #returns homepage

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
        return render_template("Articles.html",items= headline_set) #returns the headlines to Articles page






if __name__=="__main__":
    app.run(debug=True) #Runs the app
