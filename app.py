#https://webdesign.tutsplus.com/tutorials/building-a-weather-app-with-the-darksky-api--cms-28678 PRZEKSZTALCENIE LONG,LAT na nazwe miasta z google api
from flask import Flask, render_template, request
import json, time, requests, datetime

darkskyAPI = 'dacdc5620ba241a45fb5c1f5d838fdf9'

app = Flask(__name__)

@app.route("/")
def main():
    #if request.method == "POST":
    #    user_city = request_form.get("city")

    #pobieranie i przetwarzanie danych pogodowych z API
    weatherUrl = requests.get('https://api.darksky.net/forecast/' + darkskyAPI + '/51.21006,16.1619?lang=pl&units=auto&exclude=currently&exclude=minutely&exclude=hourly&exclude=alerts&exclude=flags')
    weatherRequest = weatherUrl.text
    data = json.loads(weatherRequest)
    
    #przetworzenie dat z UNIX na Datetime
    dt1 = data['daily']['data'][0]['time']
    date1 = datetime.datetime.fromtimestamp(int(dt1))
    date1 = date1.strftime('%d.%m')

    dt2 = data['daily']['data'][1]['time']
    date2 = datetime.datetime.fromtimestamp(int(dt2))
    date2 = date2.strftime('%d.%m')

    dt3 = data['daily']['data'][2]['time']
    date3 = datetime.datetime.fromtimestamp(int(dt3))
    date3 = date3.strftime('%d.%m')

    dt4 = data['daily']['data'][3]['time']
    date4 = datetime.datetime.fromtimestamp(int(dt4))
    date4 = date4.strftime('%d.%m')

    #temperatury
    today = data['daily']['data'][0]['temperatureMax']
    nextday1 = data['daily']['data'][1]['temperatureMax']
    nextday2 = data['daily']['data'][2]['temperatureMax']
    nextday3 = data['daily']['data'][3]['temperatureMax']

    return render_template("layout.html", today=round(today, 1), nextday1=round(nextday1, 1), nextday2=round(nextday2, 1), nextday3=round(nextday3, 1), date1=date1, date2=date2, date3=date3, date4=date4)

if __name__ == '__main__':
    app.run()