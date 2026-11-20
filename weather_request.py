def city_coordinates(city_name):
    import requests
    import json

    try:
        # city_name = input('Введите город: ')
        response = requests.get('https://geocode-maps.yandex.ru/'
                                '1.x/?apikey=8167a872-631d-4097-bc7f-1a51cc882733&geocode=' + city_name + '&format=json')
        response.raise_for_status()
        # if response:
        #     print('Success!')
        # else:
        #     print('Error!')
    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except json.decoder.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

    coordinates = response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']


    longitude, latitude = coordinates.split()

    # print(f"Долгота: {longitude}")
    # print(f"Широта: {latitude}")
    return longitude, latitude

# city_coordinates('Нижний Новгород')
