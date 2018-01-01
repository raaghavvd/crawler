from TwitterAPI import TwitterAPI
#Setting the OAuth

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
     print(item['text'])
     count=count+1
     if count > 19:
         break
print(count)
