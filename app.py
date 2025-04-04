from flask import Flask, render_template, request
import requests

app = Flask(__name__)

#@app.route("/")
#def hello_world():
#   return render_template('index.html') 


API_KEY = "d44a40fbd09fc85338f2bad842ad3f6d"
BASE_URL = "http://api.weatherstack.com/current"

def get_weather(city):
    params = {
        "access_key": API_KEY,
        "query": city
    }
    response = requests.get(BASE_URL, params=params)
    return response.json()

@app.route('/', methods=['GET', 'POST'])
def home():
    city = "New York"  # Default city
    if request.method == 'POST':
        city = request.form.get('city')
    weather_data = get_weather(city)
    return render_template("index.html", weather=weather_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)