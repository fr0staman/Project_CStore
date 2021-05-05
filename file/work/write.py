import json


def editing(srch):
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)
    for element in data['tovar']:
        if element['name'] == srch:
            print("Його ціна:", element['price'],
                  '\n На яку бажаєте змінити?')
            element['price'] = int(input())
            open('data.json', 'w').write(json.dumps(data, indent=1))
            return
    print("Такого нима((")


def creating():
    data = {
        "tovar": [],
        'order': []
    }
    with open("data.json", 'w') as data_file:
        json.dump(data, data_file)


def updating_t(obj):
    with open('data.json', 'r') as jfr:
        jf_file = json.load(jfr)
    with open('data.json', 'w') as jf:
        jf_target = jf_file['tovar']
        user_info = {'id': 4, 'name': obj.GetName(), 'price': obj.GetPrice(), 'number': obj.GetNumber()}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=1)


def updating_o(obj):
    with open('data.json', 'r') as jfr:
        jf_file = json.load(jfr)
    with open('data.json', 'w') as jf:
        jf_target = jf_file['order']
        user_info = {'id': 1, 'id_tovar': 4, 'count': obj.GetCoun(), 'date': obj.GetDatin()}
        jf_target.append(user_info)
        json.dump(jf_file, jf, indent=1)


def deleting(dltn):
    data = json.load(open('data.json'))
    el = data['tovar']
    for i in range(len(el)):
        if el[i]['name'] == dltn:
            data['tovar'].pop(i)
            open('data.json', 'w').write(json.dumps(data, indent=1))
            return
    print("Такого товару не існує!")