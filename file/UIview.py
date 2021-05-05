import datetime
import json
# from PySide2 import QtWidgets
# from PySide2.QtWidgets import QTableWidgetItem


from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        dat = "{\"events\": {\"050719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Sent\": \"3\", \"Date\": \"05.07.2019\"}, \"050919\": {\"Type\": \"Conference\", \"Published\": \"23\", \"Sent\": \"35\", \"Date\": \"05.09.2019\"}, \"120719\": {\"Type\": \"Conference\", \"Published\": \"3\", \"Sent\": \"4\", \"Date\": \"12.07.2019\"}, \"150719\": {\"Type\": \"Conference\", \"Published\": \"4\", \"Date\": \"15.07.2019\", \"Sent\": \"2\"}}}"
        # or
        # with open('..\data.json', 'r') as f:
        #     data = json.load(f)
        # #d = json.loads(dat)
        # keys = ["ID", "Name", "Price", "Number"]
        # labels = keys + ["ID"]
        # w.setColumnHidden(4, True)
        # w.setHorizontalHeaderLabels(labels)
        # print(enumerate(d['events'].items()))
        # print(data['tovar'][0].keys())
        # for n in range(len(data['tovar'])):
        # for i, (key, value) in enumerate(data['tovar'][0].items()):
        #    print(keys)
        #    print(value)
        #    rows = [value] + [key]
        #    w.insertRow(w.rowCount())
        #    for j, v in enumerate(rows):
        #        it = QtWidgets.QTableWidgetItem(v)
        #        w.setItem(i, j, it)
        # w = QtWidgets.QTableWidget()
        # w.setColumnHidden(4, True)
        # MainWindow.setObjectName("MainWindow")

        MainWindow.resize(800, 600)
        data = [('John', 5, 5),
                ('Rex', 5, 6),
                ('Watson', 7, 8),
                ('Manila', 9, 9),
                ('Pete', 10, 8),
                ('Mathew', 5, 7)]
        numrows = len(data)
        numcols = len(data[0])
        # numrows = len(data['tovar'])
        # numcols = len(data['tovar'][0])
        centralwidget = QtWidgets.QWidget(MainWindow)
        tableWidget = QtWidgets.QTableWidget(centralwidget)
        tableWidget.setColumnCount(3)
        tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "From"))
        item = tableWidget.horizontalHeaderItem(2)
        #item.setText(_translate("MainWindow", "To"))

        # el = data['tovar']

        for row in range(numrows):
            for column in range(numcols):
                tableWidget.setItem(row, column, QTableWidgetItem((data[row][column])))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
