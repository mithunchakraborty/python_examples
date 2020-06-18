import sys
import psycopg2
from contextlib import closing
from user import User
from table import DatabaseTable
from authorization import Authorization
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, qApp,
    QAction, QTextEdit, QTableWidget,
    QGridLayout, QWidget, QTableWidgetItem,
    QToolTip, QPushButton, QVBoxLayout,
    QMessageBox, QDesktopWidget, QLabel,
    QLineEdit, QDockWidget, QListWidget
)
from PyQt5.QtGui import (
    QIcon, QKeyEvent, QFont
)
from PyQt5.QtCore import (
    Qt, QSize,QCoreApplication
)

class Program(QMainWindow) :

    def __init__(self) :
        super().__init__()
        self.initUI()

    def initUI(self) :
        # Window config
        self.setWindowTitle("Database client")
        self.setMinimumSize(QSize(800, 500))
        self.setWindowIcon(QIcon("python.png"))
        self.setFont(QFont("SF Mono", 10))
        self.center()

        # Authorization
        self.au = Authorization(self)
        self.setCentralWidget(self.au)
        self.au.accept.clicked.connect(self.accepting)

        # Bars
        self.setMenuBar()

    def accepting(self) :
        """ Accepting account
        """
        if not self.au.login.text() :
            self.showDialog("Поле Login не может быть пустым")
        elif not self.au.password.text() :
            self.showDialog("Поле Password не может быть пустым")
        else :
            self.connectDatabase(
                self.au.login.text(),
                self.au.password.text()
            )

    def center(self) :
        """ Window on center screen
        """
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeEvent(self, event) :
        """ Close dialog window
        """
        reply = QMessageBox.question(
            self,
            "Message",
            "Вы точно хотите выйти?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes : event.accept()
        else : event.ignore()

    def connectDatabase(self, login:str, password:str) :
        """ Try to connect with database
        """
        try :
            with closing(psycopg2.connect(
                dbname="agency",
                user=login,
                password=password,
                host="localhost"
            )) as conn :
                # Create Tool bar
                self.setToolBar()

                # Create new user
                self.usr = User(login, password)

                # Create new tabs and close authorization
                self.table = DatabaseTable()
                self.setTable()

                # Set dock
                self.createDock()
        except psycopg2.OperationalError:
            self.showDialog("Неверный логин или пароль")

    def setMenuBar(self) :
        """ Set menu bar
        """
        # Exit action menu
        exitAction = QAction(
            QIcon(""),
            "Exit",
            self
        )
        exitAction.setShortcut("Ctrl+Q")
        exitAction.setStatusTip("Exit application")
        exitAction.triggered.connect(self.close)

        # Log out action menu
        logAction = QAction(
            QIcon(""),
            "Log out",
            self
        )
        logAction.setShortcut("Ctrl+O")
        logAction.setStatusTip("Log out")
        logAction.triggered.connect(self.logout)

        # Dock action menu
        dockAction = QAction(
            QIcon(""),
            "Dock tables",
            self
        )
        dockAction.setShortcut("Ctrl+D")
        dockAction.setStatusTip("Dock tables")
        dockAction.triggered.connect(self.showDock)

        # Menu bar
        menubar = self.menuBar()
        fileMenu = menubar.addMenu("&File")
        fileMenu.addAction(logAction)
        fileMenu.addAction(exitAction)
        viewMenu = menubar.addMenu("&View")
        viewMenu.addAction(dockAction)

        # Status bar
        self.statusBar().showMessage("Status Bar ready")

    def setToolBar(self) :
        """ Set tool bar
        """
        # insert action
        insertAction = QAction(
            QIcon(""),
            "Insert",
            self
        )
        insertAction.setStatusTip("Insert into table")
        insertAction.triggered.connect(self.insertIntoTable)

        # delete action
        deleteAction = QAction(
            QIcon(""),
            "Delete",
            self
        )
        deleteAction.setStatusTip("Delete from table")
        deleteAction.triggered.connect(self.deleteFromTable)

        # save action
        saveAction = QAction(
            QIcon(""),
            "Save",
            self
        )
        saveAction.setStatusTip("Save all changes")
        saveAction.triggered.connect(self.saveChanges)

        # Tool bar
        toolbar = self.addToolBar("Exit")
        toolbar.addAction(saveAction)
        toolbar.addAction(insertAction)
        toolbar.addAction(deleteAction)

    def showDock(self) :
        try :
            self.dockWidget.show()
        except AttributeError :
            self.showDialog("Список таблиц пуст")

    def createDock(self) :
        try :
            if len(self.findChildren(QDockWidget)) is 1 :
                return
            else :
                tables = self.usr.getNamesTables()
                dict_tabs = {
                    "tab%d" % i : tables[i] for i in range(len(tables))
                }

                self.dockWidget = QDockWidget('Tables', self)
                self.listWidget = QListWidget()

                for key in dict_tabs :
                    self.listWidget.addItem(dict_tabs[key])

                self.listWidget.itemDoubleClicked.connect(self.get_list_item)

                self.dockWidget.setWidget(self.listWidget)
                self.dockWidget.setFloating(False)

                self.addDockWidget(Qt.RightDockWidgetArea, self.dockWidget)
        except AttributeError :
            self.showDialog("Список таблиц пуст")

    def get_list_item(self):
        self.setTable(title=self.listWidget.currentItem().text())

    def logout(self) :
        try :
            del self.usr
            self.removeDockWidget(self.dockWidget)
            self.dockWidget.close()
            del self.dockWidget
            self.tab.close()
            del self.tab

            self.au = Authorization(self)
            self.setCentralWidget(self.au)
            self.au.accept.clicked.connect(self.accepting)
        except :
            return

    def insertIntoTable(self) :
        self.table.insertToTable()

    def deleteFromTable(self) :
        self.table.deleteFromTable()

    def saveChanges(self) :
        self.usr.updateToDatabase(window=self)
        self.usr.deleteToDatabase(window=self)
        self.usr.insertToDatabase(window=self)

    def showDialog(self, text:str) :
        dialog = QMessageBox.question(
            self, "Confirm Dialog", text,
            QMessageBox.Yes
        )

    def setTable(self, title="department") :
        self.setMinimumSize(QSize(480, 80))
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        grid_layout = QGridLayout()
        central_widget.setLayout(grid_layout)

        self.table = DatabaseTable(self)
        self.table.setColumnCount(
            len(self.usr.showColumnsFromDatabase(table=title))
        )
        self.table.setRowCount(
            len(self.usr.selectFromTable(table=title))
        )

        self.table.setHorizontalHeaderLabels(
            self.usr.showColumnsFromDatabase(table=title)
        )

        for i in range(self.table.columnCount()) :
            self.table.horizontalHeaderItem(i).setToolTip(
                "Column %d " % (i + 1)
            )
            self.table.horizontalHeaderItem(i).setTextAlignment(
                Qt.AlignHCenter
            )

            self.table.fillingTable(window=self, nametable=title)

            self.table.resizeColumnsToContents()
            grid_layout.addWidget(self.table, 0, 0)

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem
