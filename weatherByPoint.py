def weather_by_point(city):

    import requests
    import weather_request

    longitude, latitude = weather_request.city_coordinates(city)

    query = """{
      weatherByPoint(request: { lat:""" + latitude + """, lon:""" + longitude + """ }) {
        now {
          temperature
        }
      }
    }"""

    response = requests.post('https://api.weather.yandex.ru/graphql/query',
                             headers={"X-Yandex-Weather-Key": "demo_yandex_weather_api_key_ca6d09349ba0"},
                             json={'query': query})

    return response.json()['data']['weatherByPoint']['now']['temperature']

# weather_by_point()
