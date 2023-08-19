from flask import Flask,render_template,request,redirect

import requests



app = Flask(__name__)

api_key = '1d97abd33fe378120febf14c4b35166d'


@app.route('/', methods = ["GET","POST"])
def home():
    return render_template("home.html")

@app.route('/weather', methods = ["GET","POST"])
def main():
    if request.method == "POST":
        city = request.form.get("city")
        weather_data = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")

        temp = weather_data.json().get("main").get("temp")
        humi = weather_data.json().get("main").get("humidity")
        wind = weather_data.json().get("wind").get("speed")
        cityname = weather_data.json().get("name")
        sunrise = weather_data.json().get("sys").get("sunrise")
        sunset = weather_data.json().get("sys").get("sunset")
        pressure = weather_data.json().get("main").get("pressure")
        clouds = weather_data.json().get("weather")[0].get("description")

        return render_template ("main.html", box = temp, bag = humi, pen = wind, pencil = cityname,
                                rise = sunrise, set = sunset, press = pressure, clo = clouds)
    return render_template ("main.html")

@app.route('/result')
def weather():
    return render_template ("result.html")


if __name__ == "__main__":
    app.run(debug=True)