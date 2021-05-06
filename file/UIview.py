import json
from PySide2 import QtWidgets


def uivie():
    import sys

    app = QtWidgets.QApplication(sys.argv)

    dat = "{\"events\": {\"050719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Sent\": \"3\", \"Date\": \"05.07.2019\"}, \"050919\": {\"Type\": \"Conference\", \"Published\": \"23\", \"Sent\": \"35\", \"Date\": \"05.09.2019\"}, \"120719\": {\"Type\": \"Conference\", \"Published\": \"3\", \"Sent\": \"4\", \"Date\": \"12.07.2019\"}, \"150719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Date\": \"15.07.2019\", \"Sent\": \"2\"}}}"
    # or

    # print(enumerate(d['events'].items()))

    # for i, (key, value) in enumerate(data['tovar'][0].items()):
    #     print(enumerate(data['tovar'][0].items()))
    #     print(i)
    #     rows = [key] + [value]
    #     print( "Ключ:", key, "Значення:", value)
    #     w.insertRow(w.rowCount())
    #     print("Якась невідома параша:", w.rowCount())
    #     for j, v in enumerate(rows):
    #         it = QtWidgets.QTableWidgetItem(data['tovar'][i][key]
    #         w.setItem(j, i, it)
    # for i, (key, value) in enumerate(data['tovar'][0].items()):
    #    it = QtWidgets.QTableWidgetItem(data['tovar'][i][key])
    #    w.setItem(i, 0, it)

    with open('data.json', 'r') as f:
        data = json.load(f)
    d = json.loads(dat)
    keys = ["ID", "Name", "Price", "Number"]
    labels = keys + ["ID"]

    w = QtWidgets.QTableWidget()
    w.setColumnCount(4)
    w.setRowCount(4)
    w.setHorizontalHeaderLabels(labels)

    for i, (key, value) in enumerate(data['tovar'][0].items()):
        for row in range(len(data['tovar'][i])):
            it = QtWidgets.QTableWidgetItem(data['tovar'][row][key])
            w.setItem(row, i, it)
            print('Row:', row, "Column:", i)
            print('Info:', data['tovar'][row][key])

    w.resize(800, 600)
    w.show()
    sys.exit(app.exec_())