import requests
import requests_cache
import decimal 
import json 



requests_cache.install_cache(cache_name = 'image_cache', backend='sqlite', expire_after=900)




def get_image(search):

    url = "https://google-search72.p.rapidapi.com/imagesearch"

    querystring = {"q": search,"gl":"us","lr":"lang_en","num":"1","start":"0"}

    headers = {
        "X-RapidAPI-Key": "9aac146b28msha98b54ca2f39ee0p16455djsn9a0f2e345df6",
        "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()
    print(data)
    img_url = data['items'][0]['originalImageUrl'] #traversing data dictionary to get the image url
    return img_url

def get_quote():

    category = 'success'
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'uiWEnqFwzOHBu984T2GHyg==aB5sTLsHsFfJ9vpQ'}).json()
    quote = response[0]['quote']
    author = response[0]['author']
    return quote, author

data = get_quote()
quote = data[0]
author = data[1]
print(quote)
print(author)
# quote = get_quote()
# print(quote)


class JSONENcoder(json.JSONEncoder):
    def default(self, obj): #our custom method to handle encoding decimal objects 
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        return json.JSONEncoder(JSONENcoder, self).default(obj) #if its not a decimal just pass it to the default on the json.JSONEncoder