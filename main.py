import json as j
import requests as r
from urllib.request import urlretrieve
from PIL import Image
import pprint


def get_movie(movie_name):
    movies_api = "http://www.omdbapi.com/?apikey="+"3bb87208"+"&t="+movie_name
    data = r.get(movies_api)
    info = j.loads(data.text)
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(info)
    get_image(info['Poster'])

    bo_collection = str(info['BoxOffice'])
    bo_collection = bo_collection.strip('$')
    bo_collection = bo_collection.replace(',', '')
    bo_collection = int(bo_collection)


def get_image(Poster):
    urlretrieve(Poster, "poster.jpg")
    image = Image.open("poster.jpg")
    image.show()


def rate_conversion(rate, movie):
    rates_api = "https://v6.exchangerate-api.com/v6/"+api.RATE_API+"/latest/USD"
    get_rates = r.get(rates_api)
    rates = j.loads(get_rates.text)
    print(movie, ":", " ", "Rs.", rate*rates['conversion_rates']['INR'])


movie = str(input("Enter the movie name: "))
get_movie(movie)
