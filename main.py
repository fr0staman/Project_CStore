import json
from file.start import start
from file.work.write import creating

if __name__ == '__main__':
    try:
        json.load(open('data.json'))
    except:
        try:
            print("У вас чото файлу не було.\n Створюємо!")
            creating()
        except:
            print("Запустіть програму з підвищеними правами.")
    while True:
        start()
