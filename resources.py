import json
from random import randint

game_data = [
    {'town': 'Линхейм', 'is_here': False},
    {'town': 'Куртавия', 'is_here': False},
    {'town': 'Трайтгельм', 'is_here': False},
    {'town': 'алгоритмтоун', 'is_here': True}
]

def gen_resources():
    resources = ['💎 руда', '🧵 кожа', '🥫 специи', '⚓ металлы', '🌾 пшеница']
    for d in game_data:
        d['resources'] = []   
        for resource in resources:
            add_dict = {}
            add_dict['name'] = resource
            add_dict['price'] = randint(10, 100)
            add_dict['amount'] = randint(10, 1000)
            d['resources'].append(add_dict)
    with open('data.json', 'w', encoding='utf-8') as f:
        json.dump(game_data, f)


def get_data():
    with open('data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

gen_resources()
