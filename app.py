from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    today
    nextday1
    nextday2
    nextday3
    return render_template("index.html", today=today, nextday1=nextday1, nextday2=nextday2, nextday3=nextday3)
