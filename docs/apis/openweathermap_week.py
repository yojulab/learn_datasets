# https://openweathermap.org/ api 이용해 서울, 파리 금주 날씨

import requests
import json

# OpenWeatherMap API URL
API_URL = "http://api.openweathermap.org/data/2.5/forecast"

# API 키 입력
API_KEY = "your_api_key"

# 조회할 도시 이름
cities = ["Seoul,KR", "Paris,FR"]

for city in cities:
    # API 요청 파라미터 설정
    params = {
        'q': city,
        'appid': API_KEY
    }

    # API 요청
    response = requests.get(API_URL, params=params)

    # 응답 데이터를 JSON 형식으로 변환
    data = json.loads(response.text)

    # 날씨 정보 출력
    print("City: ", city)
    for i in range(5):  # 다음 5일 동안의 예보
        print("Date: ", data['list'][i]['dt_txt'])
        print("Weather: ", data['list'][i]['weather'][0]['description'])
        print("Temp: ", data['list'][i]['main']['temp'])
        print("Humidity: ", data['list'][i]['main']['humidity'])
        print("------")
