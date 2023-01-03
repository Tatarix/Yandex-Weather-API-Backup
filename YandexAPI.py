import requests
import pandas as pd
import config  #Необходимо получить токен для своего тарифа и записать его в файл config.py

def vko():
    headers = config.token
    params = {
        'lat': '55.605212', 'lon': '37.286370', 'lang': 'ru_RU'
    }
    # в переменнуй params забивай все нужные параметры по городу из раздела объект fact документации
    url = 'https://api.weather.yandex.ru/v2/informers?'
    responce = requests.get(url=url, params=params, headers=headers)
    json_res = responce.json()
    fact = json_res['fact']
    # в переменной fact я получил полностью только второй словать из ответа,
    # где значения fact (см документацию, что там есть в этом словаре)
    data = {'Температура': fact['temp'], 'Скорость ветра': fact['wind_speed'], 'Погодные условия': fact['condition']}
    return data


res_vko = list(vko().values())


# То,что ниже тут происходит преобразование в ДФ и выгрузка в эксель с переименовыванием столбцов в выгрузке
def result():
    df_vko = pd.DataFrame(res_vko).transpose()
    df_vko.columns = ['Температура', 'Скорость ветра', 'Погодные условия']
    writer = pd.ExcelWriter('test17.xlsx')
    df_vko.to_excel(writer)
    return writer.save()
result()


