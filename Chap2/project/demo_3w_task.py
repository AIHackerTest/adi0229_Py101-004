#!/usr/bin/env python3
# -*-coding:utf-8 -*-

import requests
import json


def fetch_weather(location):
    url = 'https://api.seniverse.com/v3/weather/now.json'
    param = {'key': 'wo8fpp5fhp121ioa', 'location': location}
    result = requests.get(url, params=param, timeout=1)
    rtn = result.text
    return rtn

def weather_info(rtn):
    text = json.loads(rtn)

    city = text['results'][0]['location']['name']
    weather = text['results'][0]['now']['text']
    wind_direction = text['results'][0]['now']['wind_direction']
    temperature = text['results'][0]['now']['temperature']
    update_time = text['results'][0]['last_update'][:-6].replace("T", ' ')

    simple_weather = "%s的天气状况为：%s" % (city, weather)
    weather_text = "%s的天气状况为：%s\n风向:%s风\n温度:%s摄氏度\n更新时间：%s" % (city, weather, wind_direction,
                                                           temperature, update_time)
    return simple_weather, weather_text

def main():
    histories = []
    print("""
    欢迎使用天气查询器

                - 输入城市名(beijing或北京)，查询该城市的天气；
                - 输入h,H,help,Help中的一个指令，获取帮助文档；
                - 输入history，获取查询历史；
                - 输入quit或exit，退出天气查询系统；
                                        """)
    while True:
        try:
            location = input('请输入指令或您要查询的城市名：')
            rtn = fetch_weather(location)
            simple_weather, weather_text = weather_info(rtn)
            print(weather_text)
            histories.append(simple_weather)
        except:
            if location in ['h', 'help', 'H', 'Help']:
                print("""
                - 输入城市名(beijing或北京)，查询该城市的天气；
                - 输入h,H,help,Help中的一个指令，获取帮助文档；
                - 输入history，获取查询历史；
                - 输入quit或exit，退出天气查询系统；
                                        """)
            elif location in ['history'] and len(histories) > 0:
                for hisotry in histories:
                    print(hisotry)
            elif location in ['history'] and len(histories) == 0:
                print("暂无记录")

            elif location in ['exit', 'quit']:
                exit()
            else:
                print('查询不到相关信息，请检查输入的城市')

if __name__ == "__main__":
    main()
