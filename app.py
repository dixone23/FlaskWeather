#https://webdesign.tutsplus.com/tutorials/building-a-weather-app-with-the-darksky-api--cms-28678 PRZEKSZTALCENIE LONG,LAT na nazwe miasta z google api
from flask import Flask, render_template
import json, time, requests, datetime

darkskyAPI = 'dacdc5620ba241a45fb5c1f5d838fdf9'

app = Flask(__name__)

@app.route("/")
def main():
    weatherUrl = requests.get('https://api.darksky.net/forecast/' + darkskyAPI + '/51.21006,16.1619?lang=pl&units=auto&exclude=currently&exclude=minutely&exclude=hourly&exclude=alerts&exclude=flags')
    weatherRequest = weatherUrl.text
    data = json.loads(weatherRequest)

    dt1 = data['daily']['data'][0]['time']
    date1 = time.ctime(dt1)
    date1 = time.strftime("%D")

    dt2 = data['daily']['data'][1]['time']
    date2 = time.ctime(dt2)
    date2 = time.strftime("%D")

    dt3 = data['daily']['data'][2]['time']
    date3 = time.ctime(dt3)
    date3 = time.strftime("%D")

    dt4 = data['daily']['data'][3]['time']
    date4 = time.ctime(dt4)
    date4 = time.strftime("%D")

    today = data['daily']['data'][0]['temperatureMax']
    nextday1 = data['daily']['data'][1]['temperatureMax']
    nextday2 = data['daily']['data'][2]['temperatureMax']
    nextday3 = data['daily']['data'][3]['temperatureMax']
    return render_template("layout.html", today=today, nextday1=nextday1, nextday2=nextday2, nextday3=nextday3, date1=date1, date2=date2, date3=date3, date4=date4)
