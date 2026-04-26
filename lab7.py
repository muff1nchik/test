import requests

API = "230a5cbcb7c37408ca16c4e380dfa9dc"
CITY_NAME = "Saint Petersburg"

########## Задание 2
def get_character(character_id):
    url = f"https://rickandmortyapi.com/api/character/{character_id}"
    return get_info(url)


def get_info(url, params=None):
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка")
        print(f"Ответ сервера: {response.status_code}")


def cool_print_cartoon(info):
    if info is None:
        return 
    print("Rick And Morty")
    print("Имя: ", info["name"])
    print("Статус: ", info["status"])
    print("Вид: ", info["species"])
    print("Пол: ", info["gender"])
    print("Происхождение: ", info["origin"]["name"])
    print("Локация: ", info["location"]["name"])
    print("Количество эпизодов: ", len(info["episode"]))

########## Задание 1
def get_weather(api, city_name):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api}"
    params = {
        "q": city_name,
        "appid": api,
        "units": "metric",
        "lang": "ru"
    }
    return get_info(url, params)
    
def cool_print_weather(weather):
    if weather is None:
        return
        
    print("Погода")
    print("Город: ", weather["name"])
    print("Температура: ", weather["main"]["temp"], "градусов Цельсия")
    print("Влажность: ", weather["main"]["humidity"], "%")
    print("Давление: ", weather["main"]["pressure"], "гПа")
    print("Погода: ", weather["weather"][0]["description"])


def main():
### 2 задание
    info = get_character(1)
    cool_print_cartoon(info)
    print()

### 3 задание
    weather = get_weather(API, CITY_NAME)
    cool_print_weather(weather)

main()
