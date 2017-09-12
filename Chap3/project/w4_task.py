from flask import Flask, render_template, url_for, request
import requests
import json

app = Flask(__name__)
histories = []

def fetch_weather(location):
    """fetch real time from api """
    url = 'https://api.seniverse.com/v3/weather/now.json'
    param = {'key': 'wo8fpp5fhp121ioa', 'location': location}
    result = requests.get(url, params=param, timeout=60)
    rtn = result.text

    text = json.loads(rtn)

    city = text['results'][0]['location']['name']
    weather = text['results'][0]['now']['text']
    temperature = text['results'][0]['now']['temperature']
    update_time = text['results'][0]['last_update'][:-6].replace("T", ' ')


    weather_str = u'{}的天气状况为：{} 温度:{} 摄氏度 更新时间：{} ' .format(city, weather,
                                                           temperature, update_time)
    return weather_str


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query')
def process_request():
    city = request.args.get('city')
    try:
        weather_info= fetch_weather(city)
        histories.append(weather_info)
        return render_template('query.html', weather_info=weather_info)
    except KeyError:
        if request.args.get('help') == "帮助":
            return render_template("help.html")
        elif request.args.get('history') == "历史记录":
            return render_template('history.html', histories=histories)
        else:
            return render_template('404.html', city=city)


if __name__ == "__main__":
    app.run(debug=True)
