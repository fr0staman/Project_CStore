import json


def reading():
    with open("data.json", 'r') as data_file:
        json_string = json.load(data_file)
        try:
            print("\n<-------- TOVAR -------->\n")
            for p in json_string['tovar']:
                print('ID      : ', p['id'])
                print('Name    : ', p['name'])
                print('Price   : ', p['price'])
                print('Number  : ', p['number'], "\n")
            print("\n<-------- ORDER -------->\n")
            for i in json_string['order']:
                print('ID      : ', i['id'])
                print('TovarID : ', i['id_tovar'])
                print('Count   : ', i['count'])
                print('Date    : ', i['date'], "\n")
        except:
            print("У вас щось не так з файлом...")


def searching(srch):
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
    for element in data['tovar']:
        if element['name'] == srch:
            print("Його ціна:", element['price'])
            return
    print("Такого нима((")
