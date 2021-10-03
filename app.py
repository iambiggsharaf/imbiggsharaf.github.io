# # Импортируем библиотеки
# # Штатная библиотека для работы со временем
# from datetime import datetime, date
# # Собственно клиент для space-track
# # Набор операторов для управления запросами. Отсюда нам понадобится время
# import spacetrack.operators as op
# # Главный класс для работы с space-track
# from spacetrack import SpaceTrackClient
 
# # Имя пользователя и пароль сейчас опишем как константы
# USERNAME = "sharaf.nazarov24@gmail.com"
# PASSWORD = "microsoftlumia950xl"
 
# # Для примера реализуем всё в виде одной простой функции
# # На вход она потребует идентификатор спутника, диапазон дат, имя пользователя и пароль. Опциональный флаг для последних данных tle
# def get_spacetrack_tle (sat_id, start_date, end_date, username, password, latest=False):
#     # Реализуем экземпляр класса SpaceTrackClient, инициализируя его именем пользователя и паролем
#     st = SpaceTrackClient(identity=username, password=password)
#     # Выполнение запроса для диапазона дат:
#     if not latest:
#         # Определяем диапазон дат через оператор библиотеки
#         daterange = op.inclusive_range(start_date, end_date)
#         # Собственно выполняем запрос через st.tle
#         data = st.tle(norad_cat_id=sat_id, orderby='epoch desc', limit=1, format='tle', epoch = daterange)
#     # Выполнение запроса для актуального состояния
#     else:
#         # Выполняем запрос через st.tle_latest
#         data = st.tle_latest(norad_cat_id=sat_id, orderby='epoch desc', limit=1, format='tle')
 
#     # Если данные недоступны
#     if not data:
#         return 0, 0
 
#     # Иначе возвращаем две строки
#     tle_1 = data[0:69]
#     tle_2 = data[70:139]
#     return tle_1, tle_2

# tle_1, tle_2 = get_spacetrack_tle (39084, date(2016,5,11), date(2016,5,12), USERNAME, PASSWORD)
# print (tle_1, tle_2)

# Импортируем библиотеки
# Штатная библиотека для работы со временем
from datetime import datetime, date
import time
# Ключевой класс библиотеки pyorbital
from pyorbital.orbital import Orbital
 
# Ещё одна простая функция, для демонстрации принципа.
# На вход она потребует две строки tle и время utc в формате datetime.datetime
def get_lat_lon_sgp (tle_1, tle_2, utc_time):
    # Инициализируем экземпляр класса Orbital двумя строками TLE
    orb = Orbital("N", line1=tle_1, line2=tle_2)
    # Вычисляем географические координаты функцией get_lonlatalt, её аргумент - время в UTC.
    lon, lat, alt = orb.get_lonlatalt(utc_time)
    return lon, lat, alt

now = datetime.utcnow()

data = []

f = open("data.txt")

lines = f.readlines()

for i in range(0,66843, 3):
    dict = {}
    dict['name'] = lines[i][2:]
    dict['tle1'] = lines[i + 1]
    dict['tle2'] = lines[i + 2]
    data.append(dict)

while True:
    locations = []
    for i in range(22281):
        try:
            locations.append(get_lat_lon_sgp(data[i]['tle1'], data[i]['tle2'], now))
        except:
            continue
    
    print(locations)

f.close()