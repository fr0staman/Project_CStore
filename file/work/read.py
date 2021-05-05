import json


def reading():
    with open("data.json", 'r') as data_file:
        json_string = json.load(data_file)
        try:
            print("\nTovar:\n")
            for p in json_string['tovar']:
                print('Name:', p['name'])
                print('Price:', p['price'])
                print('Number:', p['number'])
            print("\nOrders:\n")
            for i in json_string['order']:
                print('ID:', i['id'])
                print('ID Tovar:', i['id_tovar'])
                print('Count:', i['count'])
                print('Date:', i['date'])
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
