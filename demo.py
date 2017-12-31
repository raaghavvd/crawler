import urllib.request, json
i=0
page=[1,2,3]
for p in page:
    with urllib.request.urlopen("https://search.api.cnn.io/content?q=donald%20trump&size=10&from="+str(i)+"&page="+str(page)) as url:
        data_page[page] = json.loads(url.read().decode())

    page=page+1
    i=i+10
