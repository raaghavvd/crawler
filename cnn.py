import urllib.request, json
i=0
j=0
url_set=[]
headline_set=[]
with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10") as url:
    data_page1 = json.loads(url.read().decode())
    #print(data)
while i<10:
    print(i)
    url_set.append(data_page1['result'][i]['url'])
    headline_set.append(data_page1['result'][i]['headline'])
    i=i+1

with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10&from=10&page=2") as url:
    data_page2 = json.loads(url.read().decode())

while j<10:

    url_set.append(data_page2['result'][j]['url'])
    headline_set.append(data_page2['result'][j]['headline'])
    j=j+1
print(url_set)
print(headline_set)
