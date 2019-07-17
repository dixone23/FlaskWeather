from flask import Flask, render_template
import json, time, urllib.request

API = '1bzYRqzTdOmJyENfmlZY7cm24tGhf5fq'
legnica = 273127

def getCity(city_name):
    search_url = 'http://dataservice.accuweather.com/locations/v1/cities/search?apikey=1bzYRqzTdOmJyENfmlZY7cm24tGhf5fq&q=' + city_name + '&details=true'
    with urllib.request.urlopen(search_url) as search_url:
        data = json.loads(search_url.read().decode())
        city_location_key = data[0]['Key']
    return city_location_key

def getForecast(city_location_key):
    forecast_url = 'http://dataservice.accuweather.com/forecasts/v1/daily/10day/' + city_location_key + '?apikey=1bzYRqzTdOmJyENfmlZY7cm24tGhf5fq'
    with urllib.request.urlopen(forecast_url) as forecast_city:
        data = json.loads(forecast_city.read().decode())
        print(data)

app = Flask(__name__)

#@app.route("/")
def main():
    #today
    #nextday1
    #nextday2
    #nextday3
    return render_template("layout.html")#, today=today, nextday1=nextday1, nextday2=nextday2, nextday3=nextday3)

getForecast(getCity('Legnica'))
