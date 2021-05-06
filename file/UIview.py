import json
from PySide2 import QtWidgets


def uivie():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    keys = ["ID", "Name", "Price", "Number"]
    labels = keys + ["ID"]
    w = QtWidgets.QTableWidget()
    with open('data.json', 'r') as f:
        data = json.load(f)
    numcol = range(len(data['tovar'][0].items()))
    numrow = range(len(data['tovar']))
    w.setColumnCount(max(numcol)+1)
    w.setRowCount(max(numrow)+1)
    w.setHorizontalHeaderLabels(labels)
    for column, (key, value) in enumerate(data['tovar'][0].items()):
        for row in numrow:
            try:
                it = QtWidgets.QTableWidgetItem(str(data['tovar'][row][key]))
                w.setItem(row, column, it)
            except:
                print('щось є')
            # print('Row:', row, "Column:", column)
            # print('Info:', data['tovar'][row][key])

    w.resize(500, 300)
    w.show()
    sys.exit(app.exec_())