from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import (
    QTableWidget, QApplication,
    QMainWindow, QGridLayout,
    QWidget, QTableWidgetItem
)

class DatabaseTable(QTableWidget) :
    deleteIndexes = []
    insertIndexes = []

    def fillingTable(self, window, nametable="department") :
        self.currentTable = nametable

        data = window.usr.selectFromTable(table=nametable)
        columns = window.usr.showColumnsFromDatabase(table=nametable)
        rows = window.usr.selectFromTable(table=nametable)

        for i in range(len(columns)) :
            for j in range(len(rows)) :
                self.setItem(j, i, window.createItem(
                    str(data[j][i]),
                    Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable
                ))

    def insertToTable(self) :
        self.insertRow(self.rowCount())
        self.insertIndexes.append(self.rowCount() - 1)

    def deleteFromTable(self) :
        if self.selectedItems() :
            self.deleteIndexes.append(self.currentRow())
            self.removeRow(self.currentRow())

    def data(self) :
        dataList = []
        anotherData = []
        for j in range(self.rowCount()) :
            for i in range(self.columnCount()) :
                try :
                    dataList.append(
                        self.item(j, i).text()
                    )
                except :
                    dataList.append("");
            anotherData.append(tuple(dataList))
            dataList.clear()

        return anotherData
