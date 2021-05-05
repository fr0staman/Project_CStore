import json
from PySide2 import QtWidgets


def Uivie():
    import sys

    app = QtWidgets.QApplication(sys.argv)

    dat = "{\"events\": {\"050719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Sent\": \"3\", \"Date\": \"05.07.2019\"}, \"050919\": {\"Type\": \"Conference\", \"Published\": \"23\", \"Sent\": \"35\", \"Date\": \"05.09.2019\"}, \"120719\": {\"Type\": \"Conference\", \"Published\": \"3\", \"Sent\": \"4\", \"Date\": \"12.07.2019\"}, \"150719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Date\": \"15.07.2019\", \"Sent\": \"2\"}}}"
    # or
    with open('data.json', 'r') as f:
        data = json.load(f)
    d = json.loads(dat)
    keys = ["ID", "Name", "Price", "Number"]
    labels = keys + ["ID"]

    w = QtWidgets.QTableWidget(0, len(labels))
    w.setColumnHidden(4, True)
    w.setHorizontalHeaderLabels(labels)
    print(enumerate(d['events'].items()))

    for i, (key, value) in enumerate(data['tovar'][0].items()):
        print(enumerate(data['tovar'][0].items()))
        rows = [value for k in keys] + [key]
        w.insertRow(w.rowCount())
        for j, v in enumerate(rows):
            it = QtWidgets.QTableWidgetItem(v)
            w.setItem(i, j, it)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())