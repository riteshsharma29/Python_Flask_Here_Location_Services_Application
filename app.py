from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def my_form_post():
    location = request.form['text']
    URL = "https://geocode.search.hereapi.com/v1/geocode"
    api_key = 'your_api_key'  # Acquire from developer.here.com
    PARAMS = {'apikey': api_key, 'q': location}
    # sending get request and saving the response as response object
    r = requests.get(url=URL, params=PARAMS)
    data = r.json()
    latitude = data['items'][0]['position']['lat']
    longitude = data['items'][0]['position']['lng']
    return render_template('map.html',apikey=api_key,latitude=latitude,longitude=longitude)

if __name__ == '__main__':
    app.run(debug=True)