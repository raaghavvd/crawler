import urllib.request, json

url_set=[]
headline_set=[]

def append_links(val,page):
    i=0
    with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10&from="+str(val)+"&page="+str(page)) as url:
        data_page = json.loads(url.read().decode())

        while i<10:
            url_set.append(data_page['result'][i]['url'])
            headline_set.append(data_page['result'][i]['headline'])
            i=i+1
    #print(url_set)
    #print(headline_set)

pages=[1,2,3]
number_of_articles=[0,10,20]
for number,page_val in zip(number_of_articles,pages):
    append_links(number,page_val)

#print(len(url_set))
#print(len(headline_set))
