import requests
from bs4 import BeautifulSoup as BS


def times(city, month, day):
    t = requests.get(f'https://islom.uz/vaqtlar/{city}/{month}')
    html_t = BS(t.content, 'html.parser')
    for el in html_t.select('#large_screen'):
        time = el.select('.p_day, .juma')[day-1].text
        return {"bomdod": time[-36: -31],
                "quyosh": time[-30: -25],
                "peshin": time[-24: -19],
                "asr": time[-18:-13],
                "shom": time[-12:-7],
                "xufton": time[-6: -1]}

def city_code(city):
    cities = {
    "Toshkent": 27,
    "Andijon": 1,
    "Namangan": 15,
    "Farg'ona": 37,
    "Qo'qon": 26,
    "Qarshi": 25,
    "Termiz": 74,
    "Navoiy": 14,
    "Samarqand": 18,
    "Zarafshon": 61,
    "Jizzax": 9,
    "Guliston": 5,
    "Buxoro": 4,
    "Xiva": 21,
    "Nukus": 16
    }
    city_code = cities[city]
    return city_code
